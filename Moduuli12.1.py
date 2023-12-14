import requests


def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        vitsi = data["value"]
        return vitsi
    else:
        return None


def main():
    print("Tässä on satunnainen Chuck Norris -vitsi:")

    vitsi = hae_chuck_norris_vitsi()

    if vitsi:
        print(vitsi)
    else:
        print("Vitsin hakemisessa tapahtui virhe.")


if __name__ == "__main__":
    main()
