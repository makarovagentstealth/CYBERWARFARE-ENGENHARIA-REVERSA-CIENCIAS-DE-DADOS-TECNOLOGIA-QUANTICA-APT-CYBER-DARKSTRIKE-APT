import random
import time
import math

# --- Constantes e Configurações ---

# Estágios da Infecção
STAGE_NONE = "Não Infectado"
STAGE_LATENT = "Latente (Esporos Ativos)"
STAGE_SUBTLE_BLOCK = "Bloqueio Sutil (Início da Integração)"
STAGE_INTERMITTENT_CONTROL = "Controle Intermitente (Exigência de Resgate)"
STAGE_TOTAL_DOMINATION = "Domínio Total (Fantoche Biológico)"

# Tipos de Ação
ACTION_NEUTRAL = "Neutra"
ACTION_HARMFUL_UNNECESSARY = "Nociva/Desnecessária"
ACTION_CONSCIOUS_BENEFICIAL = "Consciente/Benéfica"

# Parâmetros da Simulação
INITIAL_POPULATION = 100
SIMULATION_DAYS = 150
INITIAL_HARM_FREQUENCY = 0.6 # Começa alto, representando a Terra pré-consciência
SPORES_PRESENT = True # Esporos do Codex Vermis estão no ambiente?

# Parâmetros do Codex Vermis
BASE_INFECTION_RATE = 0.05 # Chance base de infecção se exposto
INTEGRATION_PER_DAY_BASE = 0.01 # Aumento base da integração por dia
INTEGRATION_PER_HARMFUL_ACTION = 0.02 # Bônus de integração por ação nociva
INTEGRATION_REDUCTION_RESIST = 0.005 # Redução (lenta) da integração por resistência
RANSOM_HALT_INTEGRATION_FACTOR = 0.9 # Quanto o resgate reduz a progressão (0.1 = 90% de redução)

# Limiares de Integração para Estágios
THRESHOLD_LATENT = 0.01
THRESHOLD_SUBTLE_BLOCK = 0.20
THRESHOLD_INTERMITTENT_CONTROL = 0.50
THRESHOLD_TOTAL_DOMINATION = 0.90

# Parâmetros Humanos
BASE_SUSCEPTIBILITY = 0.5
WILLPOWER_RECOVERY_RATE = 0.02
WILLPOWER_DRAIN_INFECTION = 0.03
ENERGY_DRAIN_HARMFUL = 5
ENERGY_DRAIN_RANSOM = 15 # Pagar resgate custa muita energia vital
ENERGY_RECOVERY_NEUTRAL = 2
ENERGY_RECOVERY_CONSCIOUS = 4

# Parâmetros K'tharr
KTHARR_ENERGY_PER_RANSOM = 10
KTHARR_INFLUENCE_FACTOR = 0.001 # Como a energia K'tharr aumenta sua influência global

# --- Classes ---

class KtharrCollective:
    """Representa a consciência coletiva K'tharr."""
    def __init__(self):
        self.total_energy_harvested = 0.0
        self.broadcast_influence = 0.0 # Influência global

    def receive_energy(self, amount):
        """Recebe energia do pagamento de resgates."""
        self.total_energy_harvested += amount
        # A influência aumenta com a energia acumulada (com retornos decrescentes)
        self.broadcast_influence = 1 - math.exp(-KTHARR_INFLUENCE_FACTOR * self.total_energy_harvested)
        print(f"[K'THARR] Energia coletada: {self.total_energy_harvested:.1f}. Influência Global: {self.broadcast_influence:.3f}")

    def demand_ransom(self, human):
        """Emite a demanda de resgate (simulado)."""
        print(f"[K'THARR -> Humano {human.id}] ALERTA: Sofrimento crescente. Submeta-se. Gaste energia. Pague o resgate para alívio temporário.")

class Human:
    """Representa um indivíduo humano."""
    def __init__(self, id):
        self.id = id
        self.infected = False
        self.infection_stage = STAGE_NONE
        self.integration_level = 0.0 # Nível de 0.0 a 1.0
        self.susceptibility = BASE_SUSCEPTIBILITY * random.uniform(0.8, 1.2) # Variação individual
        self.willpower = random.uniform(0.5, 1.0) # Capacidade de resistir
        self.energy_level = random.uniform(80, 120)
        self.is_paying_ransom = False
        self.is_resisting = False # Está ativamente tentando ações conscientes?
        self.days_since_last_ransom_demand = 0

    def _update_stage(self):
        """Atualiza o estágio da infecção baseado na integração."""
        if self.integration_level >= THRESHOLD_TOTAL_DOMINATION:
            if self.infection_stage != STAGE_TOTAL_DOMINATION:
                 print(f"[Humano {self.id}] ALERTA: Integração completa. Vontade subjugada. {STAGE_TOTAL_DOMINATION}")
                 self.infection_stage = STAGE_TOTAL_DOMINATION
                 self.willpower = 0 # Perda total de vontade
        elif self.integration_level >= THRESHOLD_INTERMITTENT_CONTROL:
             if self.infection_stage != STAGE_INTERMITTENT_CONTROL:
                 print(f"[Humano {self.id}] ALERTA: Limiar de controle intermitente atingido. {STAGE_INTERMITTENT_CONTROL}")
                 self.infection_stage = STAGE_INTERMITTENT_CONTROL
        elif self.integration_level >= THRESHOLD_SUBTLE_BLOCK:
             if self.infection_stage != STAGE_SUBTLE_BLOCK:
                 print(f"[Humano {self.id}] AVISO: Sinais de bloqueio sutil detectados. {STAGE_SUBTLE_BLOCK}")
                 self.infection_stage = STAGE_SUBTLE_BLOCK
        elif self.integration_level >= THRESHOLD_LATENT:
            if self.infection_stage == STAGE_NONE:
                 print(f"[Humano {self.id}] AVISO: Esporos ativados. Infecção {STAGE_LATENT} iniciada.")
                 self.infection_stage = STAGE_LATENT
                 self.infected = True # Marcar como infectado aqui
        # else: Permanece não infectado ou latente inicial

    def attempt_infection(self, global_harm_frequency, ktharr_influence):
        """Tenta infectar um humano não infectado."""
        if not self.infected and SPORES_PRESENT:
            # Chance aumenta com frequência de dano global, suscetibilidade e influência K'tharr
            infection_chance = (self.susceptibility *
                                global_harm_frequency *
                                (1 + ktharr_influence) * # Influência K'tharr aumenta a chance
                                BASE_INFECTION_RATE)
            if random.random() < infection_chance:
                self.infected = True
                self.infection_stage = STAGE_LATENT # Começa latente
                self.integration_level = THRESHOLD_LATENT # Começa com integração mínima
                print(f"[Humano {self.id}] INFECTADO! Integração inicial: {self.integration_level:.3f}")
                self._update_stage()


    def perform_action(self, global_harm_frequency, ktharr_influence):
        """Simula a ação diária do humano."""
        action_type = ACTION_NEUTRAL
        choice_roll = random.random()

        if self.infection_stage == STAGE_TOTAL_DOMINATION:
            # Totalmente controlado, sempre realiza ação nociva para K'tharr
            action_type = ACTION_HARMFUL_UNNECESSARY
            print(f"[Humano {self.id}] ({self.infection_stage}) Forçado a realizar ação nociva.")
        elif self.infected:
            # Influenciado pela infecção, resistência e vontade
            # Probabilidade base de ação nociva aumenta com integração e influência K'tharr
            prob_harmful = self.integration_level * (1 + ktharr_influence) * 0.8 # Ajuste o fator 0.8
            # Resistência e vontade diminuem a chance de ação nociva
            prob_harmful *= (1 - self.willpower * 0.5) # Vontade ajuda a resistir
            if self.is_resisting:
                prob_harmful *= 0.3 # Resistência ativa reduz drasticamente

            if choice_roll < prob_harmful:
                action_type = ACTION_HARMFUL_UNNECESSARY
                print(f"[Humano {self.id}] ({self.infection_stage}) Compelido a realizar ação nociva/desnecessária.")
            elif self.is_resisting and random.random() < self.willpower: # Chance de ação benéfica se resistindo
                 action_type = ACTION_CONSCIOUS_BENEFICIAL
                 print(f"[Humano {self.id}] ({self.infection_stage}) Escolhe ativamente ação consciente/benéfica.")
            else:
                 action_type = ACTION_NEUTRAL
                 # print(f"[Humano {self.id}] ({self.infection_stage}) Realiza ação neutra.")

        elif self.is_resisting: # Não infectado, mas resistindo ativamente (consciente)
            if random.random() < 0.7: # Maior chance de ação benéfica
                action_type = ACTION_CONSCIOUS_BENEFICIAL
            else:
                action_type = ACTION_NEUTRAL
        else: # Não infectado, não resistindo (padrão)
             # Chance de ação nociva baseada na frequência global (conformidade)
            if random.random() < global_harm_frequency * 0.6: # 0.6 = fator de conformidade
                action_type = ACTION_HARMFUL_UNNECESSARY
            else:
                action_type = ACTION_NEUTRAL

        # Atualizar energia e outras estatísticas com base na ação
        if action_type == ACTION_HARMFUL_UNNECESSARY:
            self.energy_level -= ENERGY_DRAIN_HARMFUL
            self.susceptibility += 0.01 # Ações nocivas aumentam suscetibilidade futura
            self.willpower -= 0.01 # E desgastam a vontade
        elif action_type == ACTION_CONSCIOUS_BENEFICIAL:
            self.energy_level += ENERGY_RECOVERY_CONSCIOUS
            self.susceptibility -= 0.02 # Ações conscientes reduzem suscetibilidade
            self.willpower += WILLPOWER_RECOVERY_RATE # E fortalecem a vontade
        else: # Ação Neutra
            self.energy_level += ENERGY_RECOVERY_NEUTRAL

        self.energy_level = max(0, self.energy_level) # Não pode ser negativo
        self.willpower = max(0, min(1, self.willpower)) # Limites 0-1
        self.susceptibility = max(0.1, min(1.0, self.susceptibility)) # Limites

        return action_type

    def update_infection(self, action_type, ktharr_collective):
        """Atualiza o estado da infecção com base na ação e tempo."""
        if not self.infected:
            return

        if self.infection_stage == STAGE_TOTAL_DOMINATION:
             # Não há mais progressão ou pagamento de resgate possível
             self.is_paying_ransom = False
             return

        # Progressão da integração
        integration_increase = INTEGRATION_PER_DAY_BASE
        if action_type == ACTION_HARMFUL_UNNECESSARY and not self.is_paying_ransom:
            integration_increase += INTEGRATION_PER_HARMFUL_ACTION * (1 + ktharr_collective.broadcast_influence) # Ações nocivas aceleram, mais ainda com influência K'tharr

        if self.is_resisting:
             integration_increase -= INTEGRATION_REDUCTION_RESIST * self.willpower # Resistência ativa pode *reduzir* lentamente

        if self.is_paying_ransom:
            integration_increase *= (1 - RANSOM_HALT_INTEGRATION_FACTOR) # Resgate reduz drasticamente a progressão diária
            print(f"[Humano {self.id}] Pagando resgate. Progressão da infecção reduzida.")
            self.is_paying_ransom = False # Resgate é pago uma vez por ciclo de decisão


        self.integration_level += integration_increase
        self.integration_level = max(0, min(1, self.integration_level)) # Limites 0-1

        # Dreno de vontade pela infecção
        self.willpower -= WILLPOWER_DRAIN_INFECTION * self.integration_level

        self._update_stage() # Verifica se mudou de estágio

        # Lógica do Resgate
        if self.infection_stage == STAGE_INTERMITTENT_CONTROL:
            self.days_since_last_ransom_demand += 1
            # Demanda de resgate periódica ou quando a vontade/energia está baixa
            if self.days_since_last_ransom_demand > random.randint(5, 10) or self.willpower < 0.3:
                ktharr_collective.demand_ransom(self)
                self.days_since_last_ransom_demand = 0
                # Decisão de pagar resgate: Baseado na vontade vs integração
                # Maior vontade = menor chance de pagar
                # Baixa energia também aumenta a chance de pagar por desespero
                chance_to_pay = (1 - self.willpower) * 0.7 + (1 - self.energy_level/100) * 0.3
                if random.random() < chance_to_pay and self.energy_level >= ENERGY_DRAIN_RANSOM:
                    print(f"[Humano {self.id}] Cede à pressão. Pagando o resgate biológico.")
                    self.is_paying_ransom = True
                    self.energy_level -= ENERGY_DRAIN_RANSOM
                    ktharr_collective.receive_energy(KTHARR_ENERGY_PER_RANSOM)
                else:
                    print(f"[Humano {self.id}] Resiste à demanda de resgate (Vontade: {self.willpower:.2f}, Energia: {self.energy_level:.1f}).")


    def decide_resistance(self, global_harm_frequency):
        """Decide se começa ou para de resistir ativamente."""
         # Chance de começar a resistir aumenta se:
         # - Estiver infectado (mas não dominado)
         # - A frequência global de dano for alta (percepção da ameaça)
         # - Tiver alguma vontade restante
        if not self.is_resisting and self.willpower > 0.1 and self.infection_stage != STAGE_TOTAL_DOMINATION:
             chance_to_resist = 0.05 # Chance base
             if self.infected:
                 chance_to_resist += 0.1
             chance_to_resist += global_harm_frequency * 0.2 # Perigo global incentiva
             chance_to_resist *= self.willpower # Mais vontade, mais chance

             if random.random() < chance_to_resist:
                 self.is_resisting = True
                 print(f"[Humano {self.id}] ({self.infection_stage}) Decide iniciar RESISTÊNCIA ATIVA!")

        # Chance de parar de resistir se a vontade for muito baixa ou parecer fútil
        elif self.is_resisting:
             if self.willpower < 0.15 or (self.integration_level > 0.7 and random.random() < 0.1):
                 self.is_resisting = False
                 print(f"[Humano {self.id}] ({self.infection_stage}) Cessa a resistência ativa (Vontade baixa ou futilidade percebida).")


    def get_status(self):
        """Retorna uma string com o status atual."""
        status = f"ID: {self.id} | Stage: {self.infection_stage} | Integ: {self.integration_level:.3f} | "
        status += f"Will: {self.willpower:.3f} | Energy: {self.energy_level:.1f} | Resist: {self.is_resisting}"
        return status

# --- Simulação ---

class Simulation:
    def __init__(self, population_size):
        self.population = [Human(i) for i in range(population_size)]
        self.ktharr = KtharrCollective()
        self.global_harm_frequency = INITIAL_HARM_FREQUENCY
        self.day = 0

    def calculate_global_harm_frequency(self):
        """Calcula a frequência de ações nocivas na população."""
        harmful_actions = 0
        total_actions = 0 # Considerar apenas ações não-neutras? Ou todas? Vamos contar todas por enquanto.
        
        # Simples média das ações do dia anterior (ou uma média móvel seria mais realista)
        # Para simplificar, vamos usar uma proxy: média da 'propensão' a ações nocivas
        
        propensity_sum = 0
        active_population = 0
        for human in self.population:
             if human.infection_stage != STAGE_TOTAL_DOMINATION: # Dominados não contribuem para a frequência 'escolhida'
                 # Propensão = f(integração, vontade, resistência)
                 propensity = human.integration_level * (1 - human.willpower*0.5) * (1+self.ktharr.broadcast_influence)
                 if human.is_resisting:
                     propensity *= 0.3 # Resistência reduz a propensão à nocividade
                 propensity_sum += propensity
                 active_population +=1

        # Frequência global é influenciada pela média da propensão individual + um fator base de 'ruído' social
        if active_population > 0:
             average_propensity = propensity_sum / active_population
             # A frequência real tende a seguir a propensão média, com alguma inércia
             target_frequency = min(1.0, max(0.0, average_propensity * 0.8 + 0.1)) # Ajuste fatores (0.8, 0.1)
             # Movimento gradual em direção ao alvo
             self.global_harm_frequency = self.global_harm_frequency * 0.9 + target_frequency * 0.1
        
        # Garante que fique entre 0 e 1
        self.global_harm_frequency = max(0, min(1, self.global_harm_frequency))


    def run_step(self):
        """Executa um dia da simulação."""
        self.day += 1
        print(f"\n--- Dia {self.day} --- Global Harm Freq: {self.global_harm_frequency:.3f} ---")

        self.calculate_global_harm_frequency() # Atualiza antes das ações do dia
        self.ktharr.update_influence() # Atualiza influência K'tharr (mesmo que não mude muito a cada dia)

        actions_today = {ACTION_NEUTRAL: 0, ACTION_HARMFUL_UNNECESSARY: 0, ACTION_CONSCIOUS_BENEFICIAL: 0}

        for human in self.population:
             # 1. Tentativa de nova infecção se aplicável
             if not human.infected:
                 human.attempt_infection(self.global_harm_frequency, self.ktharr.broadcast_influence)
             
             # 2. Decidir sobre resistência
             human.decide_resistance(self.global_harm_frequency)

             # 3. Realizar ação diária
             action = human.perform_action(self.global_harm_frequency, self.ktharr.broadcast_influence)
             actions_today[action] += 1

             # 4. Atualizar estado da infecção (progressão, resgate)
             human.update_infection(action, self.ktharr)

             # 5. Print status individual (opcional, para debug)
             # print(human.get_status())


        print(f"Ações do Dia: Neutras={actions_today[ACTION_NEUTRAL]}, Nocivas={actions_today[ACTION_HARMFUL_UNNECESSARY]}, Conscientes={actions_today[ACTION_CONSCIOUS_BENEFICIAL]}")
        self.print_summary() # Mostra resumo a cada dia


    def print_summary(self):
        """Imprime um resumo do estado da população."""
        counts = {stage: 0 for stage in [STAGE_NONE, STAGE_LATENT, STAGE_SUBTLE_BLOCK, STAGE_INTERMITTENT_CONTROL, STAGE_TOTAL_DOMINATION]}
        total_infected = 0
        total_resisting = 0
        avg_willpower = 0
        avg_energy = 0

        for human in self.population:
            counts[human.infection_stage] += 1
            if human.infected:
                total_infected += 1
            if human.is_resisting:
                total_resisting += 1
            avg_willpower += human.willpower
            avg_energy += human.energy_level

        pop_size = len(self.population)
        avg_willpower /= pop_size
        avg_energy /= pop_size

        print("-" * 20)
        print(f"Resumo População (Dia {self.day}):")
        for stage, count in counts.items():
            print(f"  - {stage}: {count} ({count/pop_size*100:.1f}%)")
        print(f"  - Total Infectados: {total_infected} ({total_infected/pop_size*100:.1f}%)")
        print(f"  - Resistindo Ativamente: {total_resisting} ({total_resisting/pop_size*100:.1f}%)")
        print(f"  - Vontade Média: {avg_willpower:.3f}")
        print(f"  - Energia Média: {avg_energy:.1f}")
        print(f"K'tharr Energia Total: {self.ktharr.total_energy_harvested:.1f}")
        print("-" * 20)

# --- Execução ---
if __name__ == "__main__":
    print("Iniciando Simulação Codex Vermis...")
    simulation = Simulation(INITIAL_POPULATION)
    simulation.print_summary() # Estado inicial

    for i in range(SIMULATION_DAYS):
        simulation.run_step()
        time.sleep(0.1) # Pausa para legibilidade

    print("\n--- Simulação Concluída ---")
    simulation.print_summary() # Estado final
