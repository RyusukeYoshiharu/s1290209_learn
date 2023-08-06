class FrequenciesOfItems:
    def __init__(self, database, separator='\t'):
        self.database = database
        self.separator = separator

    def getFrequencies(self):
        item_freq_dict = {}

        # トランザクションデータベースから各項目の頻度を計算する
        with open(self.database, 'r') as file:
            for line in file:
                items = line.strip().split(self.separator)
                for item in items:
                    if item in item_freq_dict:
                        item_freq_dict[item] += 1
                    else:
                        item_freq_dict[item] = 1

        return item_freq_dict
