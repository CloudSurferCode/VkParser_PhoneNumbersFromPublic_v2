import vk_api
import pandas as pd
import time


vk_session = vk_api.VkApi('********', '*********')  # логин и пароль
vk_session.auth()
vk = vk_session.get_api()





def main():

    count_in = vk.groups.getMembers(group_id='**********')
    count = count_in['count']
    print(count)
    offset = 0

    i = 1

    while count > 0:

        y = vk.groups.getMembers(group_id='*******', offset=offset, fields='contacts')
        count = count - 1000
        offset = offset+1000
        time.sleep(3)
        data = y
        df = pd.io.json.json_normalize(data['items'])
        df.to_csv(r'out_{:03}.csv'.format(i), index=False)
        i += 1





if __name__ == '__main__':
    main()
