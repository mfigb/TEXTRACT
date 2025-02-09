import boto3

def extract_text_from_image(image_path):
    # Inicializa o cliente do Textract
    client = boto3.client('textract', region_name='us-east-1')

    # Lê a imagem em formato binário
    with open(image_path, 'rb') as image_file:
        image_bytes = image_file.read()

    # Chama o Textract para detectar texto
    response = client.detect_document_text(Document={'Bytes': image_bytes})

    # Extrai e exibe o texto detectado
    for item in response['Blocks']:
        if item['BlockType'] == 'LINE':
            print(item['Text'])

if __name__ == "__main__":
    extract_text_from_image('material_escolar.jpeg')