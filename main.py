import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN)
active_chat = False

cha1 = ("🦣 Радимо вам команду по скаму кацапів, якщо ви новачок, то разом з нею ви зможете зробити свій перший "
        "профіт.\nА якщо ви досвідчений воркер знайти для "
        "себе корисний інструментарій і інформацію для збільшення своїх "
        "профітів.\nУ них в команді ви зможете знайти:\n- Реквізити для прийому грошей від русні\n- Безкоштовні мануали"
        "\n- Досвідчені воркери, які допоможуть вам дійти до першого профіту, та багато корисної інформації.\n"
        "- Багато мануалів, ботів та сайтів і закритому каналі.\nДолучайтеся до української скам комюніті\n\n"
        "https://t.me/+CXulDv9DmyViMWE6")

voice_messages = {'Доброго времени суток (р)': 'AwACAgQAAxkBAAIBqWQmLr7KcjWnBPrG9waPaHmys3rSAAJyEwACXm7IU470GqyU1WUcLwQ',
                  'Приветик (р)': 'AwACAgQAAxkBAAIBr2QmLunPdGpcUMiXobtagHSe-668AAJvEwACXm7IUzBFlkbOTJ6_LwQ',
                  'Добрый день (р)': 'AwACAgQAAxkBAAIBtWQmLzk2-7BoQxgnX-x38smusKPuAAJ6EwACXm7IU49z1WJ4IwItLwQ',
                  'Доброе утро (р)': 'AwACAgQAAxkBAAIBu2QmL1y6n2dCM6w4ceLcN7sNCcjpAAJ2EwACXm7IUzIll96Ka6RzLwQ',
                  'Добрый вечер (р)': 'AwACAgQAAxkBAAIBwWQmL4KXYM6wfDBTRg7ALpYwWhNqAAJ-EwACXm7IU_myghFAlbuNLwQ',
                  'Да (р)': 'AwACAgQAAxkBAAIByGQmMK3a4_eBxnqJnX3edujpqdoiAALvEwACXm7IU_H_HbRv5Up4LwQ',
                  'Да (г)': 'AwACAgQAAxkBAAIBzmQmMNDgEGYgtNzrneWst0J229iWAAL1EwACXm7IU4IkLA-lTv5yLwQ',
                  'Нет (р)': 'AwACAgQAAxkBAAIB1GQmMO_nVqElvuR5POSAxik-eUHNAAL5EwACXm7IU2jGIgSmy1N2LwQ',
                  'Нет (г)': 'AwACAgQAAxkBAAIB2mQmMQhkNujiVsVogD_uEVhubs__AAIBFAACXm7IUxL-l6ppAsixLwQ',
                  'Хорошо (р)': 'AwACAgQAAxkBAAIB4GQmMW8GyKjVGPZEZLruiPobOJ7JAALbEwACXm7IUwbviwU0v-_WLwQ',
                  'Хорошо (г)': 'AwACAgQAAxkBAAIB5mQmMZVJjrG-SamF0J-6wBIDOnvWAALeEwACXm7IUwFEr713TZUMLwQ',
                  'Хорошо? (р)': 'AwACAgQAAxkBAAIB7GQmMbYta0M7O4cHvJpNY88SqU1SAALrEwACXm7IU2QIY3ph7eiwLwQ',
                  'Прости, но я сейчас немного занята, позже напишу': 'AwACAgQAAxkBAAIB8mQmMdtxkkJhl8t9COIEcEv54aZ0AAIFFAACXm7IU_YuzcoP4zqwLwQ',
                  'Извини, что долго не отвечала': 'AwACAgQAAxkBAAIB-GQmMiPf40UCERRozCXxe_aYfam9AAIIFAACXm7IUw95Qy2GzfDmLwQ',
                  'До завра (р)': 'AwACAgQAAxkBAAIB_mQmMjx3HhKt11D77u-QwvmpUDamAAIOFAACXm7IUytp7ieEG-5eLwQ',
                  'Пока, пока (р)': 'AwACAgQAAxkBAAICBGQmMn7e-mYMW24UZ1yf6EcOQeQcAAIUFAACXm7IU7bqSQaP47Z4LwQ',
                  'Я тебе не доверяю': 'AwACAgQAAxkBAAICCmQmMqFruK0lMuYV3nhAcLm29a0jAAInFAACXm7IU0tB8N9bry0CLwQ',
                  'Я должна доверять тебе': 'AwACAgQAAxkBAAICEGQmMq-Zr9DanO4h3FattAzo33G-AAIsFAACXm7IU2LJKGyqEt0ZLwQ',
                  'Как дела?': 'AwACAgQAAxkBAAICFmQmMvBx0NkNI67oe5P-JCxwKKNyAAIyFAACXm7IU4N6PecdfqI9LwQ',
                  'Что делаешь?': 'AwACAgQAAxkBAAICHGQmMwQ3rnVpffl0zfuMyd4S4U0sAAI2FAACXm7IU2aym6g2dKS6LwQ',
                  'Сладких снов': 'AwACAgQAAxkBAAICImQmMyhNzw3ArmujhhHj6W_4NabeAAJDFAACXm7IU-zkvE0KLGC1LwQ',
                  'Пошлых снов': 'AwACAgQAAxkBAAICKGQmMzQ9M5VqRCMzJcJzDYsVe1_6AAJHFAACXm7IU2W1XfrmIjG7LwQ',
                  'Спокойной ночи': 'AwACAgQAAxkBAAICLmQmM0yOa2IfO9c8_K5-6MRN_J2zAAI_FAACXm7IU31hKH5lF-w9LwQ',
                  'Доброй ночи.': 'AwACAgQAAxkBAAICNGQmM3UjCuvlZ_imxF2nzhFN28_2AAJHGwACqZT5U7g6KqvM7RM_LwQ',
                  'Чмоки-чмоки ( флирт + немного смех )': 'AwACAgQAAxkBAAICOmQmM4sAAcOiT6WoA_bMV0xZKdEbHQACaxQAAl5uyFOfO9yKPQOlii8E',
                  'Фильм смотрю, блин он такой классный (рассказать о фильме)': 'AwACAgQAAxkBAAICQGQmM6H3rNAJEO1TixPG9lDzBbP-AAKgFgACXm7IU0SCxTMHUJl0LwQ',
                  'Книгу читаю ,а ты?': 'AwACAgQAAxkBAAICRmQmM-Lny2no5hTVNrEbTpAQRR0xAAKaTgACXm7AU2zzTWHIFzBYLwQ',
                  'Ногти крашу ,а ты?': 'AwACAgQAAxkBAAICTGQmM-xd6n5YpuF97acyaYKHb6_2AAKvFgACXm7IUwK0sjC-vxJdLwQ',
                  'С подружками гулять собираюсь': 'AwACAgQAAxkBAAICUmQmM__e04FvZh2xcwJWm1CTKENcAAK3FgACXm7IUxu7w0wVvTw8LwQ',
                  'Блин, я не знаю что мне надеть, поможешь?': 'AwACAgQAAxkBAAICWGQmNBGU3sn0Qh2W8GeBlcFHp8qpAALHFgACXm7IU3QBi5ai0_otLwQ',
                  'Посоветуй мне фильм какой-нибудь': 'AwACAgQAAxkBAAICX2QmNHcjXLzmzl0rFhUtuHcmnbZwAAKXFwACXm7IU2PlCcYVmuF4LwQ',
                  'Посоветуй порно ( флирт смех)': 'AwACAgQAAxkBAAICZWQmNOOSU-senAX66vNKjoMFzu7UAAKkEgAC6tLJU1igS2Gbp_FQLwQ',
                  'Посоветуй сериал': 'AwACAgQAAxkBAAICa2QmNQOQIafrWlWnxX4_1BIzW8e5AAKrFwACXm7IUyrmw35RNtKrLwQ',
                  'Почему? Я тебе не нравлюсь? (Г)': 'AwACAgQAAxkBAAICcWQmNVTN8LUXQqDsjTqYjrrgysQsAALrQQAC6tLJU1890axtFNQ6LwQ',
                  'Ты мне нравишься': 'AwACAgQAAxkBAAICd2QmNWeEixUFmq_XbeEh_1Keh9kNAAI5QgAC6tLJU7kDAcL_h4m_LwQ',
                  'А ты меня любишь? Сильно-сильно?': 'AwACAgQAAxkBAAICfWQmNYq4AwXfZnUvzAn5nWhp6RlGAAJYQgAC6tLJU9sXJgh8ZxK4LwQ',
                  'Я тебя тоже люблю': 'AwACAgQAAxkBAAICg2QmNaZ1lQhG2VTSuhwUExQuOCM8AAJKQgAC6tLJU_z4bxF6CsFaLwQ',
                  'Ой, все': 'AwACAgQAAxkBAAICiWQmNgZFSGHr9fOS-PaYPtsq4XLAAAJpQgAC6tLJUwABm6DJR_GVUS8E',
                  'Ясно': 'AwACAgQAAxkBAAICj2QmNidonQbmdRalQNS1BgfjrIs-AAKaQgAC6tLJU4ncAYzGSUVOLwQ',
                  'Понятно': 'AwACAgQAAxkBAAIClWQmNjExhhl0jNvYkSYWzsHF1yOAAAKzQgAC6tLJUwsCChbwcN5CLwQ',
                  'Пошалим? ( флирт )': 'AwACAgQAAxkBAAICm2QmNnCwgPrwDbhgZzHV_5PbEELIAALEQgAC6tLJU5aZfE5k_zxQLwQ',
                  'В чем ты сейчас одет?': 'AwACAgQAAxkBAAICoWQmNoo1sdFm-XzyIzGy7oYoBH5wAALVQgAC6tLJUxekUXi5-t45LwQ',
                  'Как думаешь в чем я сейчас одета?': 'AwACAgQAAxkBAAICp2QmNpl8Etm-AAFkY7rnI1GPYrYniwAC_hYAAl5uyFO4XEPEKIPwFy8E',
                  'Не угадал ( флирт )': 'AwACAgQAAxkBAAICrWQmNq0OkKRp4KZOKBwcOcxIGnHgAAIgFwACXm7IU1D88jEG8WX_LwQ',
                  'Черное белье (описывает белье)': 'AwACAgQAAxkBAAICs2QmNuT6QPAtf8em-BVUolRrdJG3AAIuFwACXm7IUzEmjLeevOkwLwQ',
                  'Красное белье ( описывает белье )': 'AwACAgQAAxkBAAICuWQmNu7i5KMMqXAAAcReKR2MI3C54wACQhcAAl5uyFPQrOUctpX_QS8E',
                  'Белое белье ( описывает белье )': 'AwACAgQAAxkBAAICv2QmNv3IKSoZ3mjB0yyhgeIkJkPbAAJTFwACXm7IU5s637bBTnN2LwQ',
                  'Тебе нравится моя попа?': 'AwACAgQAAxkBAAICzGQmN2NVRdAda3VVq5-n_XOBVdPSAAKDHgACqZT5U0N_cOgn11JaLwQ',
                  'Тебе нравится моя грудь?': 'AwACAgQAAxkBAAIC0mQmN24jkzkH1jPHbt5AKJwH2rUAA1kdAALq0tFTOq8QF4fTllcvBA',
                  'Скинь фоточку, я хочу его увидеть': 'AwACAgQAAxkBAAIC2GQmN5qdeZDv4UHEPFcw2flNYD0PAAL7QgAC6tLJUwFwBfZyDS-cLwQ',
                  'Уф, какой большой. Хочу тебя!': 'AwACAgQAAxkBAAIC3mQmN6xaL5LGRY_XG-8Wv6x-vzQfAALvGwAC6tLRU9rAQKl1p4mWLwQ',
                  'Я бы взяла его в ротик': 'AwACAgQAAxkBAAIC5GQmOBWns7Kg8LradkFc_GJ7YdmFAAKQHQAC6tLRUygDX7qUNM1xLwQ',
                  'Оу, я потекла благодаря тебе': 'AwACAgQAAxkBAAIC6mQmOCT293iR5D2AT_PHxK1vm99NAAKpIQACqZT5U2gxRP-64mLuLwQ',
                  'я вся горю (стоны импровизация )': 'AwACAgQAAxkBAAIC8GQmODksIikT20IJcJM-YeN-x6BNAAJzIQACqZT5U3zJjjS9du8GLwQ',
                  'Я вся мокрая   (флирт + немного стоны)': 'AwACAgQAAxkBAAIC9mQmOEQZUhaJuo0Qjf--4fUKj8ejAAKUIQACqZT5U8iSDEkw1-IzLwQ',
                  'Уф,я очень сильно хочу тебя': 'AwACAgQAAxkBAAIC_GQmOJ2pL0wVj036N1eiIw6aDDnRAAI-IQACqZT5U8T9G7vyYhCILwQ',
                  'Ты хочешь меня?': 'AwACAgQAAxkBAAIDAmQmON8d2EDHpmu3v5R2PclkyvZNAAK7HgACqZT5U0Ogtorc8SkHLwQ',
                  'Тебя нужно наказать! ( флирт )': 'AwACAgQAAxkBAAIDCGQmOPKWapFsuZ8vS47kT5Gj2rR6AAJDGgACqZT5U0KY48jGq0eBLwQ',
                  'Накажи меня ( флирт )': 'AwACAgQAAxkBAAIDDmQmOP9hBNLqcQfc5UpTt7dFgBT5AAKMGgACqZT5U_s9kRYS5syzLwQ',
                  'Меня нужно наказать? Нет! Я хорошая. Наверно. (флирт+ смех)': 'AwACAgQAAxkBAAIDGmQmOZZI2b4YcW8KX7sJwJT5ZVHLAAJhGgACqZT5U6h1gdPUn20fLwQ',
                  'Зайчик, ты где?': 'AwACAgQAAxkBAAIDIGQmOcDEjpGuIwtdu3ObKPvBVGtlAAIlHgAC6tLRUxTnAxf6lWdqLwQ',
                  'Котик, ты где?': 'AwACAgQAAxkBAAIDJ2QmOdd51CvaJlWTD43ji5nDvBMnAALyMwAC6tLRU92TK8IH3zo0LwQ',
                  'Ты где? Мурр': 'AwACAgQAAxkBAAIDLWQmOhSi5jGH7c5-6nnxIjaX86jPAAJ6NAAC6tLRU6yBmAKAaChOLwQ',
                  'Только из душа вышла': 'AwACAgQAAxkBAAIDM2QmOlyAPpnHWZjPJEMtt57T_sVTAAI2GQACqZT5U1gnFsEWhrekLwQ',
                  'Я сейчас в ванной, блин обожаю пену': 'AwACAgQAAxkBAAIDOWQmOpnnIGMxCZLdd_dy-AsqZZwlAAJJGQACqZT5U6TUgBBOIDxNLwQ',
                  'Что делаю? Та,  Кушать готовлю': 'AwACAgQAAxkBAAIDP2QmOrYi4_ZF3prLLQqIhcnWNdEIAAKEGQACqZT5U83_BmEzNJY9LwQ',
                  'Между прочем я очень вкусно готовлю еще ни кто не жаловался  и летальных исходов не было.': 'AwACAgQAAxkBAAIDRWQmO7tQv0CJOv3uMTumZPdlhvEIAALqGQACqZT5U7ERARdFg4hsLwQ',
                  'Хочешь со мной  готовить?  Мы можем вместе что-нибудь жарить ( смех + флирт )': 'AwACAgQAAxkBAAIDbmQmQJGlb5a6uuofJOEhqAubfnsXAAKzGQACqZT5U08-sY14MQiHLwQ',
                  'Рассказать о блюде любом (  описать какое вкусное )': 'AwACAgQAAxkBAAIDdGQmQK2wz-UCq2DSXxVbf502-AKPAAIDGgACqZT5U9mmuFwJTP-QLwQ',
                  'Я очень люблю готовить.': 'AwACAgQAAxkBAAIDemQmQL6nayTzopHHDYWQjx4SnQJ8AAIXGgACqZT5U3cxUii0Y30rLwQ',
                  'Извини, у меня есть маленькая просьба к тебе. Можешь помочь пожалуйста денежкой? Буду очень благодарна.': 'AwACAgQAAxkBAAIDgGQmQNvKAn1lA2giRl1VL3vWomWMAAK3HAACqZT5U1rHO8CwydcnLwQ',
                  'Как скинешь - обязательно отпиши': 'AwACAgQAAxkBAAIDhmQmQOqDnN5babGFeKD15n-vnddzAAL-HgACqZT5U-0gvF40huyjLwQ',
                  'Очень выручил, я твоя должница. Проси все что хочешь.': 'AwACAgQAAxkBAAIDjGQmQeNrO2WqJi9V8qkmGx2Me-mJAALXNAAC6tLRU9oaNEBBGzxALwQ',
                  'Что ты хочешь взамен?': 'AwACAgQAAxkBAAIDkmQmQfAO4d20zWfya9Lje_lzS8PuAALDGgACqZT5U2BQOTjLlNr1LwQ',
                  'Зайка..': 'AwACAgQAAxkBAAIDmWQmQh2nB8qebCEP-_CW54RC33ehAAJgGwACqZT5U6y_Tix96j68LwQ',
                  'Солнышко..': 'AwACAgQAAxkBAAIDn2QmQihef6ad7tGEThjBPkGwDhpJAAJ-GwACqZT5UwlJzr2_XzO-LwQ',
                  'Котик..': 'AwACAgQAAxkBAAIDpWQmQjUqPg-YaYj8ZfDLyolSzdoGAAK7GwACqZT5U6FBIRUqvtQ1LwQ',
                  'Я тут вино пью красное и мне кажется я немного пьяненькая уже ( попробовать икнуть )': 'AwACAgQAAxkBAAIDq2QmQpztCc8DPn-DnNtjSWA_AVqvAAI2HAACqZT5U02QzKI4Alv_LwQ',
                  'Почему ты мне не отправляешь смайлики? (Г очень)': 'AwACAgQAAxkBAAIDsWQmQrpFSdhU0_keooWCC9Dsq2hiAAIoQgAC6tLJUwABbgXJnmjKxS8E',
                  'Я обиделась (Г)': 'AwACAgQAAxkBAAIDt2QmQt9nm4spU4gx-NEiSJ8noGBRAAIMQgAC6tLJU8GOvT7jQ9FnLwQ',
                  'Блин, мне немного грустно': 'AwACAgQAAxkBAAIDvWQmQu-4rtBJlNlsoHPZQJ08aBd2AAI6FAACXm7IUwqTwrIhfrBjLwQ',
                  'Как день прошел?': 'AwACAgQAAxkBAAIDw2QmQvqk75u_6tGweqvHuytlXcRZAAIrNQAC6tLRU5BVU1qMPsfGLwQ',
                  'Хочешь я приеду?': 'AwACAgQAAxkBAAIDyWQmQ5F0OsvHRh1B8nD-t8lhUYlNAAJYNQAC6tLRU1b6zuU2sqKnLwQ',
                  'Скоро буду, жди..': 'AwACAgQAAxkBAAIDz2QmQ59nRVxA7mTQt8P2uL322NCWAALxGAACqZT5U-5Yr6sWTZW6LwQ',
                  'Благодарю': 'AwACAgQAAxkBAAID1WQmQ7BpPy3DJU_p7oJcPROfQ0vDAAKmNAAC6tLRU_yswJ6WhJOxLwQ',
                  'Спасибо большое очень приятно (р)': 'AwACAgQAAxkBAAID22QmQ7z4LX6JupLbsIewZraSz8FrAAIOIAACqZT5UyxoF3WZYw1HLwQ',
                  'Спасибо': 'AwACAgQAAxkBAAID4WQmQ8ZC8v74DAAB8QZMS3UdCqcAAdQAAjYgAAKplPlTacq4YQxN0PwvBA',
                  'Я соскучилась очень сильно, забыл за меня?  (г)': 'AwACAgQAAxkBAAID52QmRCtEtiK2nTGIn1soZgnRDeazAAJiHwACqZT5UwPJHLS9i5LcLwQ',
                  'Расскажи, мне интересно': 'AwACAgQAAxkBAAID7WQmRDgyAAHZryQwz21KeZ-791CC5AACGxQAAl5uyFOM3oG6ENZFti8E',
                  'Для меня это в новинку': 'AwACAgQAAxkBAAID82QmRERBDW-KeYxlPsKoDBvA5vDwAAIgFAACXm7IU2UTZWWfWs2sLwQ',
                  'Договорились (р)': 'AwACAgQAAxkBAAID-WQmRFLkDhmN4mTVpYP-4E0-ussyAAI2TAACXm7AUyCXmAJImLmaLwQ',
                  'Очень жаль (г)': 'AwACAgQAAxkBAAID_2QmRF6U3G0HLJB4bHfRuA72TBsaAALIEwACXm7IUxcGQg5E0H1hLwQ',
                  'Буду ждать (р)': 'AwACAgQAAxkBAAIEBWQmRKhuKIYhYog-qlCmfgU8U16TAALSEwACXm7IUzYfXd25W-IJLwQ',
                  'Буду ждать (г)': 'AwACAgQAAxkBAAIEC2QmRLfVioammptBputTX-z5rqJAAALYEwACXm7IUzy6ZoX2MIwoLwQ',
                  'Подожди': 'AwACAgQAAxkBAAIEEWQmRMOGiNLGMkPZ1NYMxXz2P3Y1AAIkFAACXm7IU5vwqX-vlFWtLwQ',
                  'Пожалуйста.. ( Г)': 'AwACAgQAAxkBAAIEF2QmRNn9orsygX1WuhKs_syhSMJSAAIHGQACqZT5UzmYfwuFBg1RLwQ',
                  'Обидно (г)': 'AwACAgQAAxkBAAIEHWQmRO4iAAE3BxCfeDZbmtdw8F0IywACDRQAAl5uyFNTipojXcQx1i8E',
                  'Ну,блинннн ( очень капризным голосом )': 'AwACAgQAAxkBAAIEJWQmRR3wAAHyhM6_d_VpvU77Eb8igQACDhwAAqmU-VMGxBz7FPj2pC8E',
                  'Мурр..': 'AwACAgQAAxkBAAIEK2QmRWzYehXOCXMRezL8wXDtMmbyAALgHQAC6tLRU6OoJe1JnU6mLwQ',
                  'Ну, Котик…мурр': 'AwACAgQAAxkBAAIEMWQmRXvfvKC0rikSN_Tfx9uz4Qu1AALAHQAC6tLRU-phRf7JD1jlLwQ',
                  'К сожалению, не могу (г)': 'AwACAgQAAxkBAAIEN2QmRZCHL42KdnCQd_CT3--Xk7wdAAKpEwACXm7IUxElVq-sEZIlLwQ',
                  'Не поняла': 'AwACAgQAAxkBAAIEPWQmRZ7tIjq4vYnfT6ezUAu1JBV_AAIiFAACXm7IU0mCY8tm2OcdLwQ',
                  'Я очень сильно устала (описывает, как прошел день)': 'AwACAgQAAxkBAAIEQ2QmRbKr3AWLc5CjU51_UNcVCSggAAJvFwACXm7IU7w_1-znEtzCLwQ',
                  'Мне очень плохо я наверно спать пойду (девушка рассказывает, что болит)': 'AwACAgQAAxkBAAIESWQmRcOLPWbXn2q8RP8eBceUNcFPAAKAFwACXm7IU_4LtWsVy6LdLwQ',
                  'Покидай музыки': 'AwACAgQAAxkBAAIET2QmRc7xwkvmyRjqh9jRhXZcctSnAALLQQAC6tLJUxGm5VkQfu4zLwQ'}


def main_menu(message, msg="Главное меню:"):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = types.KeyboardButton("Паки моделей)")
    itembtn2 = types.KeyboardButton("Голосовые Сообщения")
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')


def send_voice_message(chat_id, voice_id):
    voice_file = bot.get_file(voice_messages[voice_id])
    bot.send_voice(chat_id, voice_file.file_id)


def send_keyboard_markup(chat_id, msg):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add("Главное меню", "Вступ до команди🇺🇦", "Ламповый чат🌌")
    for voice_id in voice_messages:
        button = telebot.types.KeyboardButton(voice_id)
        markup.add(button)
    bot.send_message(chat_id, msg, reply_markup=markup)


@bot.message_handler(commands=["start"])
def start(message):
    global active_chat
    active_chat = True
    msg = "Поздравляем! Вы подписались на Женские голосовые Pro.\n\nИспользуйте /off чтобы приостановить подписку."
    main_menu(message, msg)


@bot.message_handler(commands=["off"])
def stop_bot(message):
    global active_chat
    active_chat = False
    chat_id = message.chat.id
    msg = "Ваша подписка деактивирована.\n\nВы всегда можете включить ее снова с помощью команды /start."
    markup = types.ReplyKeyboardRemove()
    bot.send_message(chat_id, msg, reply_markup=markup)


def add_voice_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Send me the name of the voice message to add.")
    bot.register_next_step_handler(message, add_voice_name)


def add_voice_name(message):
    chat_id = message.chat.id
    voice_name = message.text

    if voice_name in voice_messages:
        bot.send_message(chat_id, "Error: Voice message with that name already exists.")
    else:
        bot.send_message(chat_id, "Now send me the voice message to add.")
        bot.register_next_step_handler(message, add_voice_file, voice_name)


def add_voice_file(message, voice_name):
    chat_id = message.chat.id
    if message.content_type == "voice":
        voice = message.voice
        voice_id = voice.file_id

        temp = {str(voice_name): str(voice_id)}
        voice_messages.update(temp)
        bot.send_message(chat_id, "Voice message added successfully.")
        print(f"voice_messages = {voice_messages}\n\n")
    else:
        msg = "Error: Message type is not voice. Try to send voice message again"
        bot.send_message(chat_id, msg)


@bot.message_handler(commands=['add_voice'])
def handle_add_voice_command(message):
    add_voice_message(message)


@bot.message_handler(func=lambda message: active_chat, content_types=["text"])
def messages(message):
    if message.text == "Паки моделей)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        itembtn1 = types.KeyboardButton("Главное меню")
        markup.add(itembtn1)
        msg = ("https://t.me/+Eb5Nli0RUvkyZTg6\n\n\nКупить паки(зборку) фото и видео девушек для *роботы можно тут: "
               "\n\n""https://t.me/+Eb5Nli0RUvkyZTg6\n\n*Паки созданы для продажи интим фото и видео, "
               "но каждый может использовать как хочет🙂")
        bot.send_message(message.chat.id, msg, reply_markup=markup, parse_mode='html')
    elif message.text == "Голосовые Сообщения":
        msg = "Тут премиум зборка"
        send_keyboard_markup(message.chat.id, msg)
    elif message.text == "Главное меню":
        main_menu(message)
    elif message.text in voice_messages:
        send_voice_message(message.chat.id, message.text)
    elif message.text == "вигруз":
        print(f"voice_messages = {voice_messages}")
    elif message.text == "Вступ до команди🇺🇦":
        ph_id = "AgACAgIAAxkBAAIBdWQmJ78YfW93qLmqr1ffbivZjLWLAAJMyTEbUAYxSZ4WLCZLniXSAQADAgADcwADLwQ"
        bot.send_photo(message.chat.id, ph_id)
        bot.send_message(message.chat.id, cha1, parse_mode='html')
    elif message.text == "Ламповый чат🌌":
        msg = "https://t.me/+eH3x8jamFIEwNmM6"
        bot.send_message(message.chat.id, msg, parse_mode='html')
    else:
        msg = "Извините, я вас не понял. Возвращаюсь на Главное меню."
        main_menu(message, msg)


@bot.message_handler(content_types=["photo"])
def photo_id(message):
    bot.send_message(message.chat.id, message, parse_mode='html')


bot.infinity_polling()
