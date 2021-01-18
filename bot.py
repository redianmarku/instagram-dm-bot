from instadm import InstaDM
import time
import schedule


with open(r'users.txt', 'r') as f:
    users = [line.strip() for line in f]

print(users)

# Auto login
insta = InstaDM(username='arndomguy', password='deK5345bJk434./3r4', headless=False)

def scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)


def msg():
    for user in users:  
        # Send message
        insta.sendMessage(user=user, message="Pleasure, say hello to the IG bot, gonna disturb you every damn day. What's next is the for every liked feature; a comment about the debt you keep avoiding for all to see. Oh well, you caused this ")
        

schedule.every().day.at("01:05").do(msg)
schedule.every().day.at("01:35").do(msg)
schedule.every().day.at("02:05").do(msg)
schedule.every().day.at("02:35").do(msg)
schedule.every().day.at("03:05").do(msg)
schedule.every().day.at("03:35").do(msg)
schedule.every().day.at("04:05").do(msg)
schedule.every().day.at("04:35").do(msg)
schedule.every().day.at("05:05").do(msg)
schedule.every().day.at("05:35").do(msg)
schedule.every().day.at("06:05").do(msg)
schedule.every().day.at("06:35").do(msg)
schedule.every().day.at("07:05").do(msg)
schedule.every().day.at("07:35").do(msg)
schedule.every().day.at("08:05").do(msg)
schedule.every().day.at("08:35").do(msg)
schedule.every().day.at("09:05").do(msg)
schedule.every().day.at("09:35").do(msg)
schedule.every().day.at("10:05").do(msg)
schedule.every().day.at("10:35").do(msg)
schedule.every().day.at("11:05").do(msg)
schedule.every().day.at("11:35").do(msg)
schedule.every().day.at("12:05").do(msg)
schedule.every().day.at("12:35").do(msg)
schedule.every().day.at("13:05").do(msg)
schedule.every().day.at("13:35").do(msg)
schedule.every().day.at("14:05").do(msg)
schedule.every().day.at("14:35").do(msg)
schedule.every().day.at("15:05").do(msg)
schedule.every().day.at("15:35").do(msg)
schedule.every().day.at("16:05").do(msg)
schedule.every().day.at("16:35").do(msg)
schedule.every().day.at("17:05").do(msg)
schedule.every().day.at("17:35").do(msg)
schedule.every().day.at("18:05").do(msg)
schedule.every().day.at("18:35").do(msg)
schedule.every().day.at("19:05").do(msg)
schedule.every().day.at("19:35").do(msg)
schedule.every().day.at("20:05").do(msg)
schedule.every().day.at("20:35").do(msg)
schedule.every().day.at("21:05").do(msg)
schedule.every().day.at("21:35").do(msg)
schedule.every().day.at("22:05").do(msg)
schedule.every().day.at("22:35").do(msg)
schedule.every().day.at("23:05").do(msg)
schedule.every().day.at("23:35").do(msg)
schedule.every().day.at("00:05").do(msg)
schedule.every().day.at("00:35").do(msg)


if __name__ == '__main__':
    msg()
    scheduler()

