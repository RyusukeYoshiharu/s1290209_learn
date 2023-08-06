import plotly.express as px

class HeatMapItemsFrequencies:
    def __init__(self, items_frequencies_dict):
        self.items_frequencies_dict = items_frequencies_dict

    def plotHeatMap(self):
        # itemsFrequenciesDictionaryから地図のプロット用のデータを整理
        latitudes = []
        longitudes = []
        frequencies = []

        for item, frequency in self.items_frequencies_dict.items():
            latitude, longitude = item
            latitudes.append(latitude)
            longitudes.append(longitude)
            frequencies.append(frequency)

        # ヒートマップのプロット
        fig = px.density_mapbox(
            lat=latitudes,
            lon=longitudes,
            z=frequencies,
            radius=10,
            center=dict(lat=sum(latitudes) / len(latitudes), lon=sum(longitudes) / len(longitudes)),
            mapbox_style="open-street-map",
            zoom=10,
            opacity=0.7,
        )

        # プロットを表示
        fig.show()

if __name__ == "__main__":
    from frequenciesOfItems import FrequenciesOfItems

    # トランザクションデータベースファイル名とセパレータを指定
    transactional_database = "transactional_database.txt"
    separator = "\t"

    # FrequenciesOfItemsのインスタンスを生成し、頻度の辞書を取得
    items_frequencies = FrequenciesOfItems(transactional_database, separator)
    items_freq_dictionary = items_frequencies.getFrequencies()

    # HeatMapItemsFrequenciesのインスタンスを生成し、ヒートマップをプロット
    heat_map = HeatMapItemsFrequencies(items_freq_dictionary)
    heat_map.plotHeatMap()

