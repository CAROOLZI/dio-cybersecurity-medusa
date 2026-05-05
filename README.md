

🚀 Automação de Testes de Segurança com Python e Medusa
📋 Descrição do Projeto
Este projeto demonstra a integração de scripts Python para automação de massas de dados (wordlists) e o uso da ferramenta Medusa para auditoria de segurança em serviços SSH.

🧠 Raciocínio Lógico e Decisões Técnicas
Otimização de Hardware: O ambiente foi configurado utilizando WSL2 (Kali Linux) em um notebook com 4GB de RAM e processador Intel Celeron N4000. A escolha pelo WSL2 visou a máxima eficiência de recursos, evitando o overhead de máquinas virtuais pesadas.

Automação com Python: Desenvolvi um script (gerador.py) para criar uma wordlist personalizada. Isso demonstra um pensamento de QA, onde a massa de dados é controlada e estratégica, em vez de depender de arquivos massivos que comprometeriam a performance do hardware.

Análise de Infraestrutura: Durante os testes, identifiquei e documentei a necessidade de provisionamento do serviço openssh-server para validar a conectividade na porta 22.

🛠️ Tecnologias Utilizadas
Python 3: Geração dinâmica de credenciais.

Medusa: Auditoria de força bruta em protocolos de rede.

WSL2 / Kali Linux: Ambiente de execução.

Linux Terminal (Bash): Gerenciamento de pacotes e serviços.
