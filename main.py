from slovar import COUNTRY, A_CODES, A_COUNTRY


class iPhone:
    def __init__(self):
        self.model_num = None

    def info_by_number_model(self, model: str):
        self.model_num = model
        result = {}

        if model[0] == 'M':
            result['State'] = 'Brand new machine'
            return self._get_county(result)
        elif model[0] == 'F':
            result['State'] = 'The device has been officially refurbished under the Apple Certified Refurbished program'
            return self._get_county(result)
        elif model[0] == 'P':
            result['State'] = 'New engraved smartphone'
            return self._get_county(result)
        elif model[0] == 'N':
            result['State'] = 'The device was provided as a replacement for a faulty iPhone'
            return self._get_county(result)
        elif model[0] == 'A':
            return self._short_model(result)
        else:
            result['State'] = None
            return self._get_county(result)

    def _get_county(self, result):
        model = self.model_num
        check_country = model.split('/')
        model = check_country[0]

        con = f'{model[-2]}{model[-1]}'
        if con in COUNTRY:
            result['Country'] = COUNTRY[con]
        elif model[-1] in COUNTRY:
            result['Country'] = COUNTRY[model[-1]]
        else:
            result['Country'] = None

        return result

    def _short_model(self, result):
        model = self.model_num
        result['Model'] = None

        if model[0] == 'A':
            for i in list(A_CODES.values()):
                if model in i:
                    key = self._get_key(A_CODES, model)
                    result['Model'] = key

            if model in A_COUNTRY:
                result['Country'] = A_COUNTRY[model]
            else:
                result['Country'] = None

        return result

    def _get_key(self, damn, value):
        for k, v in damn.items():
            if value in v:
                return k


if __name__ == '__main__':
    p = iPhone()
    a = p.info_by_number_model('MH2N4VN/A')
    print(a)
