import client

class RobotCakru:
    
    sudahBuat = False

    def __init__(self, nama=None):
        if(not(RobotCakru.sudahBuat)):
            if(nama==None):
                print('Harus ada namanya')
            else:
                self.nama = nama
                client.kirimPesan('URO '+self.nama+' buat 0')
                RobotCakru.sudahBuat = True
        else:
            print('Kamu sudah menginisialisasi robotnya tadi')

    def status(self):
        if(RobotCakru.sudahBuat):
            stat = client.kirimPesan('URO '+self.nama+' status 0').split(' ')
            data = {}
            data['Posisi'] = [int(stat[0]),int(stat[1])]
            data['Arah'] = float(stat[2])
            data['HP'] = float(stat[3])
            data['Ammo'] = int(stat[4])
            return data
        else:
            print('Buat dulu robotnya')

    def maju(self, banyak):
        if(RobotCakru.sudahBuat):
            client.kirimPesan('URO '+self.nama+' maju '+str(banyak))
        else:
            print('Buat dulu robotnya')

    def putarCW(self, banyak):
        if(RobotCakru.sudahBuat):
            client.kirimPesan('URO '+self.nama+' putarCW '+str(banyak))
        else:
            print('Buat dulu robotnya')
    
    def putarCCW(self, banyak):
        if(RobotCakru.sudahBuat):
            client.kirimPesan('URO '+self.nama+' putarCCW '+str(banyak))
        else:
            print('Buat dulu robotnya')

    def majuPutar(self, banyakMaju, banyakPutar):
        if(RobotCakru.sudahBuat):
            client.kirimPesan('URO '+self.nama+' majuPutar '+str(banyakMaju)+' '+str(banyakPutar))
        else:
            print('Buat dulu robotnya')

    def tembak(self):
        if(RobotCakru.sudahBuat):
            client.kirimPesan('URO '+self.nama+' tembak 0')
        else:
            print('Buat dulu robotnya')