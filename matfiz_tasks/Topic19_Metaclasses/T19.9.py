def decorator_type(Cls):
    class NewCls(object):
        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                print("Incorrect Attribute!")
                exit(0)
            x = self.oInstance.__getattribute__(s)
            print(type(x))

    return NewCls

@cls_dec
class Rlist:
    '''Р РµР°Р»С–Р·СѓС” РєС–Р»СЊС†РµРІРёР№ СЃРїРёСЃРѕРє РЅР° Р±Р°Р·С– СЃРїРёСЃРєСѓ.
    '''
    def __init__(self):
        '''РЎС‚РІРѕСЂРёС‚Рё РїРѕСЂРѕР¶РЅС–Р№ СЃРїРёСЃРѕРє.
        '''
        self._lst = []                  #СЃРїРёСЃРѕРє РµР»РµРјРµРЅС‚С–РІ
        self._cur = None                #С–РЅРґРµРєСЃ РїРѕС‚РѕС‡РЅРѕРіРѕ РµР»РµРјРµРЅС‚Р°

    def len(self):
        return len(self._lst)

    def next(self):
        l = self.len()
        if l != 0:
            if self._cur == l-1:
                self._cur = 0
            else:
                self._cur += 1

    def getcurrent(self):
        if self.len() == 0:
            print('getcurrent: СЃРїРёСЃРѕРє РїРѕСЂРѕР¶РЅС–Р№')
            exit(1)
        data = self._lst[self._cur]
        return data

    def update(self, data):
        if self.len() == 0:
            print('update: СЃРїРёСЃРѕРє РїРѕСЂРѕР¶РЅС–Р№')
            exit(1)
        self._lst[self._cur] = data

    def insert(self, data):
        if self.len() == 0:
            self._lst.append(data)
            self._cur = 0
        else:
            self._lst.insert(self._cur, data)
            self._cur += 1

    def delete(self):
        if self.len() == 0:
            print('delete: СЃРїРёСЃРѕРє РїРѕСЂРѕР¶РЅС–Р№')
            exit(1)
        l = self.len()
        del self._lst[self._cur]
        if l == 1:
            self._cur = None
        elif self._cur == l-1:
            self._cur = 0
        #else: pass

    def __del__(self):
        del self._lst


obj = Rlist()
Rlist.save('output.txt')
# obj.save('output.txt')
# obj.save('output.txt')

