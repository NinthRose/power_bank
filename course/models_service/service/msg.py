from twilio.rest import Client

# account_sid = 'AC78c6331498337142a53dbe406fbddff9'
# auth_token = '1f6b1615f88fb8d661bfdbaf4eb40ee7'
# from_phone = '+15306257454'
# PHONE_PREFIX = '+86'
# client = Client(account_sid, auth_token)
# MSG = '【亲爱的撼舞街舞会员{}】您本次消费：正课{}节(剩余{}节)，免费赠送课时{}节(剩余{}节)，联系电话：18712760616'
# MSG = 'good {}.{},{}.{}.{}'
#
#
# def send_msg(lessons, free, rest, rest_free, name, phone):
#     return client.messages.create(from_=from_phone, body=MSG.format(name, lessons, rest, free, rest_free),
#                                   to=PHONE_PREFIX + phone)
#
#
# msg = send_msg(1, 2, 3, 4, '师重启宝宝', '15313135514')
# # msg = send_msg(1, 2, 3, 4, '师重启宝宝', '18712760616')
# print(msg.sid)
