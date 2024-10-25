class Sorvete:
    def __init__(self):
        self.preco_base = 0
        self.preco_recipiente = 0
        self.preco_cobertura = 0

    def calcular_preco(self, tipo, recipiente, cobertura):
        # Define preço base pelo tipo
        if tipo.lower() == "comum":
            self.preco_base = 15
        elif tipo.lower() == "premium":
            self.preco_base = 20
        else:
            raise ValueError("Tipo de sorvete inválido")

        # Adiciona preço do recipiente
        if recipiente.lower() == "copinho":
            self.preco_recipiente = 1
        elif recipiente.lower() == "casquinha":
            self.preco_recipiente = 2
        else:
            raise ValueError("Tipo de recipiente inválido")

        # Adiciona preço da cobertura
        if cobertura.lower() == "simples":
            self.preco_cobertura = 1
        elif cobertura.lower() == "especial":
            self.preco_cobertura = 2
        elif cobertura.lower() == "sem":
            self.preco_cobertura = 0
        else:
            raise ValueError("Tipo de cobertura inválido")

        # Calcula preço final
        preco_final = self.preco_base + self.preco_recipiente + self.preco_cobertura
        return preco_final


# Exemplo de uso
if __name__ == "__main__":
    sorvete = Sorvete()

    # Alguns exemplos
    print("Sorvete Comum, Copinho, Cobertura Simples:")
    print(f"R${sorvete.calcular_preco('comum', 'copinho', 'simples')}")

    print("\nSorvete Premium, Casquinha, Cobertura Especial:")
    print(f"R${sorvete.calcular_preco('premium', 'casquinha', 'especial')}")

    print("\nSorvete Premium, Copinho, Sem Cobertura:")
    print(f"R${sorvete.calcular_preco('premium', 'copinho', 'sem')}")