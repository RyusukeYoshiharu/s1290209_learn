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
            # itemの情報を取得（仮定：itemは緯度・経度のタプル (latitude, longitude) とする）
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
    # テスト用のitemsFrequenciesDictionaryデータ（仮定：緯度・経度のタプルをキーとして頻度を値とする辞書）
    items_frequencies_dict = {
        (35.6895, 139.6917): 100,  # 東京の緯度経度と頻度
        (40.7128, -74.0060): 80,   # ニューヨークの緯度経度と頻度
        # 他の緯度経度と頻度のデータが続く
    }

    # HeatMapItemsFrequenciesのインスタンスを生成し、ヒートマップをプロット
    heat_map = HeatMapItemsFrequencies(items_frequencies_dict)
    heat_map.plotHeatMap()

