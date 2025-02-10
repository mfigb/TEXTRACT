# Importação da biblioteca boto3, que é a SDK oficial da AWS para Python. 
# Permite interagir com os serviços da AWS, como o Textract.
import boto3

# A função extract_text_from_image recebe um caminho para uma imagem (image_path) como argumento.
def extract_text_from_image(image_path):
    
    # Inicializa o cliente do Textract e especifica a região us-east-1 onde o serviço do Textract será acessado
        client = boto3.client('textract', region_name='us-east-1')

    # Lê a imagem em formato binário('rb') e armazena o mesmo em image_bytes.
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    # Chama o Textract para detectar texto. O método processa a imagem e retorna uma resposta com as informações de texto que ele conseguiu detectar.   
    response = client.detect_document_text(Document={'Bytes': image_bytes})

    # Extrai e exibe o texto detectado
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            print(item['Text'])

# A função extract_text_from_image() é executada apenas quando o script for rodado diretamente (e não quando for importado como módulo em outro script) e é chamada passando o caminho da imagem ('material_escolar.jpeg').

if __name__ == "__main__":
    extract_text_from_image('material_escolar.jpeg')


