import local_settings
from django.contrib.auth import get_user_model
from crud.models import Farm, SoilUser, Pivots
from django.contrib.auth.hashers import make_password, mask_hash, check_password

class SaveInitialData:
    
    def __init__(self, data):
        self.data = data
        if self.data:
            print("Dados recebidos com sucesso salvando na memória...")
            self.__user()
            self.__owner()
            self.__dealer()
            self.__users()
            self.__farm()
            self.__pivots()
    
    
    def __adapter_user(self, user):
        try:
            
            exists = SoilUser.objects.filter(username=user["username"]).first()
    
            if not exists:
                user_type = user["user_type"]
                print(f"Criando {user_type} da fazenda")
                SoilUser.objects.create(
                    username=user["username"],
                    password=user["password"],
                    user_type=user_type,
                    user_id=user["user_id"],
                    is_superuser=False,
                    is_staff=False,
                    is_active=False,
                )
            return self
        except Exception as error:
            print("Error ....................")
            print(error)
            
            
    def __user(self):
        try:
            sudo = self.data.get("SUDO")
            if not sudo:
                return self
            print("Verificando existencia de usuário sudo".upper())
            exists = get_user_model().objects.filter(username=sudo["username"]).first()
            
            if not exists:
                print("Criando usuário".upper())
                get_user_model().objects.create_superuser(
                    username=sudo["username"],
                    password=sudo["password"],
                    user_type=sudo["user_type"],
                    user_id=sudo["user_id"],
                    is_superuser=True,
                    is_staff=True,
                    is_active=True,
                )
                print("Usuario master criado com sucesso".upper())
            
            
            return self
        except Exception as error:
            print("Error ....................")
            print(error)
            
            
    def __owner(self):
        try:
            
            owner = self.data.get("OWNER")
            
            if not owner:
                return self
            
            self.__adapter_user(owner)
            return self
        except Exception as error:
            print("Error ....................")
            print(error)
    
    
    def __farm(self):
        try:
            
            farm = self.data.get("FARM")
            
            if not farm:
                return self
            
            exists = Farm.objects.filter(farm_id=farm["farm_id"]).first()
            
            if not exists:
                print("Criando dados da fazenda")

                
                f= Farm.objects.create(
                    farm_id=farm["farm_id"],
                    user_id=SoilUser.objects.filter(user_id=farm["user_id"]).first(),
                    farm_name=farm["farm_name"],
                    farm_city=farm["farm_city"],
                    farm_lat=farm["farm_lat"],
                    farm_lng=farm["farm_lng"],
                    dealer=SoilUser.objects.filter(user_id=farm["dealer"]).first() if farm["dealer"] else None,
                    
                )
                if farm["users"] and len(farm["users"]) > 0:
                    for user in farm["users"]:
                        f.add(SoilUser.objects.filter(user_id=user["user_id"]).first())
                
            return self
        except Exception as error:
            print("Error ....................")
            print(error)

    
    def __dealer(self):
        try:
            dealer = self.data.get("DEALER")
            if not dealer:
                return self
            
            self.__adapter_user(dealer)
            return self
        except Exception as error:
            print("Error ....................")
            print(error)
            
            
    def __users(self):
        try:
            users = self.data.get("USERS")
            
            if not users or len(users) <= 0:
                return self
            
            for user in users:
                self.__adapter_user(user)
                
            return self
        except Exception as error:
            print("Error ....................")
            print(error)
            
            
    def __pivots(self):
        try:
            pivots = self.data.get("PIVOTS")
            
            if not pivots or len(pivots) <= 0:
                return self
            
            for pivot in pivots:
                exists = Pivots.objects.filter(pivot_id=pivot["pivot_id"]).first()
            
                if not exists:
                    num = pivot["pivot_num"]
                    print(f"Criando pivô {num}")
                    
                    
                    Pivots.objects.create(
                        farm_id=Farm.objects.filter(farm_id=pivot["farm_id"]).first(),      
                        pivot_id=pivot["pivot_id"],
                        pivot_num=pivot["pivot_num"],
                        pivot_is_gprs=pivot["is_gprs"],
                        radio_id=pivot["radio_id"],
                        pivot_ip_gateway=pivot["ip_gateway"],
                        pivot_lat=pivot["pivot_lat"],
                        pivot_lng=pivot["pivot_lng"],
                        pivot_end_angle=pivot["pivot_end_angle"],
                        pivot_start_angle=pivot["pivot_start_angle"]  
                    )
                
            return self
        except Exception as error:
            print("Error ....................")
            print(error)

  
    