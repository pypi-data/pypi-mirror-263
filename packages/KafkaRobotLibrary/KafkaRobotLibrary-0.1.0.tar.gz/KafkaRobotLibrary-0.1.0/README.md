
# KafkaLibrary para Robot Framework

`KafkaLibrary` é uma biblioteca do Robot Framework que permite a interação fácil com o Apache Kafka, possibilitando a produção e consumo de mensagens dentro de testes automatizados.

## Instalação

Para instalar a `KafkaLibrary`, simplesmente execute:

```bash
pip install KafkaLibrary
```

Certifique-se de que a versão do Python e do pip estão atualizadas para evitar quaisquer incompatibilidades.

## Configuração

Para utilizar a `KafkaLibrary` em seus testes, você precisa inicializá-la com a configuração do seu servidor Kafka. Isso pode ser feito ao importar a biblioteca em seu arquivo `.robot`, especificando os parâmetros necessários:

```robot
*** Settings ***
Library    KafkaLibrary    bootstrap_servers=localhost:9092    sasl_mechanism=PLAIN    security_protocol=SASL_PLAINTEXT    sasl_plain_username=user    sasl_plain_password=password
```

## Keywords

### `Create Producer`

Inicializa um produtor Kafka para enviar mensagens. Chamada opcional, pois `Send Message` irá inicializá-lo se necessário.

**Uso:**

```robot
Create Producer
```

### `Send Message`

Envia uma mensagem JSON para um tópico Kafka especificado.

**Argumentos:**
- `topic`: Nome do tópico Kafka.
- `message`: Mensagem JSON como string.

**Exemplo:**

```robot
Send Message    topic=meu_topico    message={"chave": "valor"}
```

### `Consume Messages`

Consome e retorna mensagens de um tópico Kafka.

**Argumentos:**
- `topic`: Nome do tópico Kafka.
- `group_id`: ID do grupo de consumidores.
- `limit` (opcional): Número máximo de mensagens a consumir (padrão 1).

**Exemplo:**

```robot
@{messages}=    Consume Messages    topic=meu_topico    group_id=meu_grupo_id    limit=1
Log    ${messages}
```

## Contribuindo

Encorajamos contribuições! Se você tem ideias para melhorias, novas funcionalidades ou encontrou um bug, sinta-se à vontade para abrir uma issue ou um pull request no repositório do GitHub.

## Licença

Distribuída sob a licença MIT. Consulte o arquivo `LICENSE` no repositório GitHub para mais informações.
