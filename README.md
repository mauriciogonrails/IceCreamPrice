# Sistema de Precificação de Sorvetes 🍦

## Descrição
Este projeto implementa um sistema de precificação para uma sorveteria, calculando o preço final do sorvete com base em três critérios principais: tipo do sorvete, recipiente e cobertura.

## Estrutura de Preços

### Tipos de Sorvete
- **Comum**: R$15,00
- **Premium**: R$20,00

### Recipientes
- **Copinho**: Adiciona R$1,00
- **Casquinha**: Adiciona R$2,00

### Coberturas
- **Simples** (uma cobertura): Adiciona R$1,00
- **Especial** (duas ou mais coberturas): Adiciona R$2,00
- **Sem Cobertura**: Não adiciona valor

## Complexidade Ciclomática
O sistema possui uma complexidade ciclomática de 4, calculada através da fórmula:
- Número de nós prediais (decisões) + 1
- Nós prediais: 3 (tipo de sorvete, recipiente, cobertura)
- Complexidade final: 3 + 1 = 4

## Tecnologias Utilizadas
- Python 3.x
- Programação Orientada a Objetos

## Como Usar

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/precificacao-sorveteria.git

# Entre no diretório
cd precificacao-sorveteria
```

### Exemplo de Uso
```python
from sorvete import Sorvete

# Cria uma instância da classe Sorvete
sorvete = Sorvete()

# Calcula o preço de diferentes combinações
preco = sorvete.calcular_preco('comum', 'copinho', 'simples')
print(f"Preço do sorvete: R${preco}")  # Resultado: R$17
```

### Parâmetros Aceitos

1. **Tipo de Sorvete**
   - 'comum'
   - 'premium'

2. **Recipiente**
   - 'copinho'
   - 'casquinha'

3. **Cobertura**
   - 'simples'
   - 'especial'
   - 'sem'

## Exemplos de Preços

| Tipo    | Recipiente | Cobertura | Preço Final |
|---------|------------|-----------|-------------|
| Comum   | Copinho    | Simples   | R$17,00     |
| Premium | Casquinha  | Especial  | R$24,00     |
| Premium | Copinho    | Sem       | R$21,00     |

## Tratamento de Erros
O sistema inclui validação para entradas inválidas e lançará `ValueError` com mensagens específicas em caso de:
- Tipo de sorvete inválido
- Recipiente inválido
- Tipo de cobertura inválido

## Estrutura do Código
```python
class Sorvete:
    def __init__(self):
        self.preco_base = 0
        self.preco_recipiente = 0
        self.preco_cobertura = 0
    
    def calcular_preco(self, tipo, recipiente, cobertura):
        # Implementação do cálculo de preço
```

## Contribuindo
1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Possíveis Melhorias Futuras
- Interface gráfica para usuário
- Persistência de dados
- Sistema de pedidos
- Relatórios de vendas
- Integração com sistema de pagamento

## Licença
Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autor
Mauricio Gomes - [mauriciolxrdev@gmail.com](mailto:mauriciolxrdev@gmail.com)


