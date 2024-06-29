from foto.models import Client, Discount


async def check(user_id):
    client = Client.objects.get(id=user_id)
    dacoin_general = 0
    dacoin_foto = 0
    dacoin_pay = 0
    dacoin_bot = 0
    dacoin_like = 0
    dacoin_otzivi = 0
    
    if client.dacoin_general == True:
        dacoin_general = 1
    if client.dacoin_foto == True:
        dacoin_foto = 1
    if client.dacoin_pay == True:
        dacoin_pay = 1
    if client.dacoin_bot == True:
        dacoin_bot = 1
    if client.dacoin_like == True:
        dacoin_like = 2
    if client.dacoin_otzivi == True:
        dacoin_otzivi = 3
    
    total_dacoin = dacoin_general + dacoin_foto + dacoin_pay + dacoin_bot + dacoin_like + dacoin_otzivi
    
    try:
        discount_obj = Discount.objects.get(id=user_id)
        discount = discount_obj.percent
    except:
        discount = 0
    return total_dacoin, discount


async def change(user_id, total_coin):
    client = Client.objects.get(id=user_id)
    #Дописать Если существует скидка для данного клиента
    try:
        discount = Discount.objects.get(id=user_id)
        discount.percent = total_coin
        discount.save()
    except:
        discount = Discount.objects.create(
            id=user_id,
            username=client.username,
            password=f'tgokmnjiuhb{client.username}{total_coin}',
            percent=total_coin
            )
    client.dacoin_general = False
    client.dacoin_foto = False
    client.dacoin_pay = False
    client.dacoin_bot = False
    client.dacoin_like = False
    client.dacoin_otzivi = False
    client.save()
    return discount.percent, discount.password