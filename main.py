import requests

def get_proxies():
    try:
        response = requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&simplified=true')
        proxies = response.text.split('\r\n')
        return proxies
    except Exception as e:
        print('Error al obtener proxies:', e)
        return []

def save_proxies_to_file(proxies, filename):
    try:
        with open(filename, 'w') as file:
            file.write('\n'.join(proxies))
        print('Proxies guardados en', filename)
    except Exception as e:
        print('Error al guardar proxies en el archivo:', e)

def main():
    proxies = get_proxies()
    print('Proxies disponibles:', len(proxies))
    if proxies:
        print('Ejemplo de proxy:', proxies[0])

        # Guardar proxies en un archivo de texto
        save_proxies_to_file(proxies, 'proxies.txt')

if __name__ == "__main__":
    main()
