import time

class TV:
    def __init__(self, canal="1", volume="50"):
        self.canal = canal
        self.volume = volume
     
    @property
    def canal(self):
        return self.__canal
     
    @canal.setter
    def canal(self, numero):

        if numero.isdigit():
            num = int(numero)

            if num > 0 and num <= 150:
                self.__canal = num
            else:
                print('Canal inválido')
        
        else:
            print('O canal deve ser apenas em números!')
    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, numero):

        if numero.isdigit():
            num = int(numero)
            if num >= 0 and num <= 100:
                self.__volume = num
            else:
                print('O volume deve ser entre 0 e 100')
        else:
            print('O volume deve ser apenas numeros')

    def mudaCanal(self):
        num = input('Mudar para o canal: ')
        self.canal = num

    def mudaVolume(self):
        num = input('Mudar para o volume: ')
        self.volume = num

    def __str__(self):
        return (f'canal: {self.canal} /nvolume: {self.volume}/n ')

def main():
    tv01 = TV()

    while True:
        print('/n'*40)
        print(tv01)

        print('Opções ----------')
        print('1 - mudar canal')
        print('2 - mudar volume')
        print('3 - desligar/n -------------')
        selec = input('Selecionar:')

        if selec == "1":
            tv01.mudaCanal()
            
        elif selec == "2":
            tv01.mudaVolume()

        elif selec == "3":
            print('Desligando ....')
            break
        else:
            print('Selecione uma opção valida')
            
        time.sleep(2)
            

main()

    