import nextcord
import datetime


class HelpCommand(nextcord.ui.Select):
    def __init__(self):

        selectOps = [
            nextcord.SelectOption(
                emoji="<:media:1097192443499266058>", label="Главное меню ➲", description="Начало всех начал.."
            ),
            nextcord.SelectOption(
                emoji="<:student_cur:1097192375698337792>", label="Информация ➲", description="Помощь по информации."
            ),
            nextcord.SelectOption(
                emoji="<:pictures:1097192472670646352>", label="Утилиты ➲", description="Помощь по утилитам."
            ),
            nextcord.SelectOption(
                emoji="<:event:1097192407570849864>", label="Развлечения ➲", description="Помощь по развлечениям."
            ),
            nextcord.SelectOption(
                emoji="<:event:1097192407570849864>", label="Развлечения (continuation) ➲", description="Помощь по развлечениям 2-й список."
            ),
            nextcord.SelectOption(
                emoji="<:moon:1097192356865921084>", label="Модерация ➲", description="Помощь по модерации."
            ),
            nextcord.SelectOption(
                emoji="<:tribunemode:1097192458946887791>", label="RolePlay ➲", description="Помощь по РП."
            ),
            nextcord.SelectOption(
                emoji="<:tribunemode:1097192458946887791>", label="RolePlay (continuation) ➲", description="Помощь по РП 2-й список."
            ),
            nextcord.SelectOption(
                emoji="<:tribunemode:1097192458946887791>", label="RolePlay (continue) ➲", description="Помощь по РП 3-й список."
            ),
            nextcord.SelectOption(
                emoji="<:developer:1097192560696500234>", label="Административное ➲", description="Помощь для Администрации серверов."
            ),
            nextcord.SelectOption(
                emoji="<:18yo:1097192487715606539>", label="RolePlay 18+ ➲", description="Помощь по пошлых РП."
            ),
        ]
        super().__init__(
            placeholder="Выберите категорию",
            min_values=1,
            max_values=1,
            options=selectOps,
        )

    async def callback(self, interaction: nextcord.Interaction):
        page1 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Тут описаны все команды <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page1.add_field(
            name="> <:student_cur:1097192375698337792> Информация (BETA) ➲",
            value="`.banner` `.uptime` `.avatar` `.helpserver` `.server` `.prefix` `.user`",
            inline=False,
        )
        page1.add_field(name="> <:pictures:1097192472670646352> Утилиты (BETA) ➲", value="`.embed` `.say` `.translate`", inline=False)
        page1.add_field(
            name="> <:event:1097192407570849864> Развлечения (BETA) ➲",
            value="`.hello` `.megaping` `.ktoowner` `.norm` `.cho_delaesh` `.communicate` `.bye` `.xz` `.shapi` `.bob` `.tekashi69` `.morgen` `.bbt` `.kizaru` `.lilpump` `.lilpeep` `.falls` `.squirrel` `.tom` `.tsoy` `.skala` `.fox` `.wolf` `.xxxtentacion` `.trippie` `.rabbit` `.yzhik` `.kira` `.lilnasx` `.topic` `.tesla`",
            inline=False,
        )
        page1.add_field(
            name="> <:moon:1097192356865921084> Модерация (BETA) ➲", value="`.ban` `.kick` `.clear`", inline=False,
        )
        page1.add_field(
            name="> <:tribunemode:1097192458946887791> RolePlay (BETA) ➲",
            value="`.hug` `.slap` `.kiss` `.lewd` `.angry` `.kill` `.poke` `.pat` `.bite` `.feed` `.smile` `.lick` `.wave` `.yes` `.no` `.wink` `.cry` `.smug` `.cuddle` `.dance` `.sing` `.facepalm` `.jump` `.sip` `.yawn` `.shrug` `.drink` `.dab` `.nom` `.nosebleed` `.run` `.sleep` `.stare` `.laugh` `.yaoicuddle` `.yaoihug` `.yuricuddle` `.yurihug` `.yaoikiss` `.yeet` `.highfive` `.massage` `.marry` `.merkel` `.merkel` `.reward` `.squish` `.bonk` `.yurikiss` `.arrest` `.awkward` `.ghoul`",
            inline=False,
        )
        page1.add_field(
            name="> <:developer:1097192560696500234> Административное (BETA) ➲",
            value="`.embed` `.say` `.ping`",
            inline=False,
        )
        page1.add_field(
            name="> <:18yo:1097192487715606539> RolePlay 18+ (BETA) ➲",
            value="`.sixnine` `.assfuck` `.assgrab` `.blowjob` `.bondage` `.boobsgrab` `.boobsuck` `.creampie` `.cum` `.dickride` `.facesit` `.finger` `.footjob` `.fuck` `.furryfuck` `.handjob` `.leash` `.masturbate` `.pussyeat` `.spank` `.strip` `.tittyfuck` `.yaoifuck` `.yurifuck`",
            inline=False,
        )
        page1.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page2 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по Информации <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page2.add_field(
            name=".banner",
            value="Вывести баннер пользователя!\n`.banner [пользователь]`",
            inline=False,
        )
        page2.add_field(
            name=".uptime",
            value="Посмотреть аптайм бота!\n`.uptime`",
            inline=False,
        )
        page2.add_field(
            name=".avatar", value="Вывести аватарку пользователя!\n`.avatar [пользователь]`", inline=False,
        )
        page2.add_field(
            name=".helpserver",
            value="Присоединиться на сервер разработчика!\n`.helpserver`",
            inline=False,
        )
        page2.add_field(
            name=".server",
            value="Посмотреть статистику сервера!\n `.server`",
            inline=False,
        )
        page2.add_field(
            name=".prefix",
            value="Узнать префикс бота! (если забыли)\n `.prefix`",
            inline=False,
        )
        page2.add_field(
            name="user",
            value="Узнать о пользователе!\n `.user` [пользователь]",
            inline=False,
        )
        page2.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page3 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по Утилитам <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page3.add_field(
            name=".embed",
            value="Создать вложение.\n`.embed название | описание`",
            inline=False,
        )
        page3.add_field(
            name=".say",
            value="Сказать что-то.\n`.say [текст]`",
            inline=False,
        )
        page3.add_field(
            name=".translate",
            value="Перевести англиский текст на русский!\n `.translate [англ текст]`",
            inline=False,
        )
        page3.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page4 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по Развлечениям <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page4.add_field(name=".hello", value="Привет! Как дела?\n`.hello`", inline=False)
        page4.add_field(
            name=".megaping", value="mega-pong 🏓\n`.megaping`", inline=False,
        )
        page4.add_field(
            name=".ktoowner",
            value="Мой создатель (Elezthem#3448) 💙💛\n`.ktoowner`",
            inline=False,
        )
        page4.add_field(name=".norm", value="Это хорошо, у меня тоже?\n`.norm`", inline=False)
        page4.add_field(name=".cho_delaesh", value="Я жду пока мой хозяйн меня докодит), а ты?\n`.cho_delaesh`", inline=False)
        page4.add_field(
            name=".communicate", value="Поняла, принятного общения с друзьями\n`.communicate`", inline=False,
        )
        page4.add_field(
            name=".bye",
            value="Поки, если хочешь еще пообщаться то пиши, я рада с всеми общаться)\n`.bye`",
            inline=False,
        )
        page4.add_field(
            name="xz",
            value="||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||||||:white_large_square:||\n`.xz`",
            inline=False,
        )
        page4.add_field(
            name=".shapi",
            value="Шни Шна Шнапи | Шнапи Шнапи Шнап | Шни Шна Шнапи | Шнапи Шнапи Шнап.\n `.shapi`",
            inline=False,
        )
        page4.add_field(
            name=".bob",
            value="✨ Рандомная гифка с губкой бобом!\n `.bob`",
            inline=False,
        )
        page4.add_field(
            name=".tekashi69",
            value="✨ Рандомная гифка с Tekashi 6ix9ine!\n `.tekashi69`",
            inline=False,
        )
        page4.add_field(
            name=".morgen",
            value="✨ Рандомная гифка с Morgenshternom!\n `.morgen`",
            inline=False,
        )
        page4.add_field(
            name=".bbt",
            value="✨ Рандомная гифка с Big Baby Tape!\n `.bbt`",
            inline=False,
        )
        page4.add_field(
            name=".kizaru",
            value="✨ Рандомная гифка с kizaru!\n `.kizaru`",
            inline=False,
        )
        page4.add_field(
            name=".lilpump",
            value="✨ Рандомная гифка с Lil Pump!\n `.lilpump`",
            inline=False,
        )
        page4.add_field(
            name=".lilpeep",
            value="✨ Рандомная гифка с Lil Peep!\n `.lilpeep`",
            inline=False,
        )
        page4.add_field(
            name=".falls",
            value="✨ Рандомная гифка с Graffiti Falls!\n `.falls`",
            inline=False,
        )
        page4.add_field(
            name=".squirrel",
            value="✨ Рандомная гифка с Белкой!\n `.squirrel`",
            inline=False,
        )
        page4.add_field(
            name=".tom",
            value="✨ Рандомная гифка с Tom and Jerry!\n `.tom`",
            inline=False,
        )
        page4.add_field(
            name=".tsoy",
            value="✨ Рандомная гифка с Цой!\n `.tsoy`",
            inline=False,
        )
        page4.add_field(
            name=".skala",
            value="✨ Рандомная гифка с Скалой Джонсоном!\n `.skala`",
            inline=False,
        )
        page4.add_field(
            name=".fox",
            value="✨ Рандомная гифка с Лисой!\n `.fox`",
            inline=False,
        )
        page4.add_field(
            name=".wolf",
            value="✨ Рандомная гифка с Волком!\n `.wolf`",
            inline=False,
        )
        page4.add_field(
            name=".xxxtentacion",
            value="✨ Рандомная гифка с XXXTENTACION!\n `.xxxtentacion`",
            inline=False,
        )
        page4.add_field(
            name=".trippie",
            value="✨ Рандомная гифка с Trippie Redd!\n `.trippie`",
            inline=False,
        )
        page4.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page10 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по Развлечениям (2-й список) <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page10.add_field(
            name=".rabbit",
            value="✨ Рандомная гифка с Кроликом!\n `.rabbit`",
            inline=False,
        )
        page10.add_field(
            name=".yzhik",
            value="✨ Рандомная гифка с Ыжиком!\n `.yzhik`",
            inline=False,
        )
        page10.add_field(
            name=".kira",
            value="💢 Узнать с каким процентом вы станите Кирой!\n `.kira`",
            inline=False,
        )
        page10.add_field(
            name=".lilnasx",
            value="✨ Рандомная гифка с Lil Nas X!\n `.lilnasx`",
            inline=False,
        )
        page10.add_field(
            name=".topic",
            value="🍧 Умер чат, не знаешь что делать? Используй эту команду!\n `.topic`",
            inline=False,
        )
        page10.add_field(
            name=".tesla",
            value="✨ Рандомная гифка с Tesla!\n `.tesla`",
            inline=False,
        )
        page10.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page5 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по модерации <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page5.add_field(
            name=".ban",
            value="Забанить пользователя!\n`.ban [пользователь] [причина]`",
            inline=False,
        )
        page5.add_field(
            name=".kick",
            value="Кикнуть пользователя!\n`.kick [пользователь] [причина]`",
            inline=False,
        )
        page5.add_field(
            name=".clear",
            value="Очистка сообщений!\n`.clear [кол-во сообщений]`",
            inline=False,
        )
        page5.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page6 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по РП <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page6.add_field(
            name=".hug",
            value="👐 Обнять пользователя!\n`.hug [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".slap",
            value="🖐 Ударить пользователя!\n`.slap [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".kiss",
            value="❤️ Поцеловать пользователя!\n`.kiss [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".lewd",
            value="😊 Смутиться на пользователя!\n`.lewd [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".angry",
            value="😠 Разозлиться на пользователя!\n`.angry [пользовтель] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".kill",
            value="💀 Убить пользователя!\n`.kill [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".poke",
            value="👉 Тыкнуть пользователя!\n `.poke [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".pat",
            value="🤗 Погладить пользователя!\n `.pat [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".bite",
            value="😈 Укусить пользователя!\n `.bite [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".feed",
            value="🍕 Накормить пользователя!\n `.feed [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".smile",
            value="🙂 Улыбнутся перед пользователем!\n `.smile [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".lick",
            value="😛 Облизать пользователя!\n `.lick [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".wave",
            value="👋 Приветствовать пользователя!\n `.wave [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".yes",
            value="👍 Согласиться с мнением!\n `.yes`",
            inline=False,
        )
        page6.add_field(
            name=".no",
            value="👎 Не согласиться с мнением!\n `.no`",
            inline=False,
        )
        page6.add_field(
            name=".wink",
            value="😉 Подмигнуть пользователю!\n `.wink [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".cry",
            value="😢 Поплакать...\n `.cry`",
            inline=False,
        )
        page6.add_field(
            name=".smug",
            value="😊 Выглядеть самодовольно!\n `.smug`",
            inline=False,
        )
        page6.add_field(
            name=".cuddle",
            value="😛👐 Прижиматься к пользователю!\n `.cuddle [пользователь] [комментарий]`",
            inline=False,
        )
        page6.add_field(
            name=".dance",
            value="💃 Начать танцевать!\n `.dance`",
            inline=False,
        )
        page6.add_field(
            name=".sing",
            value="🎙 Начать петь!\n `.sing`",
            inline=False,
        )
        page6.add_field(
            name=".facepalm",
            value="🤦 Словить фэйспалм",
            inline=False,
        )
        page6.add_field(
            name=".jump",
            value="🦘 Прыгнуть отсюда!\n `.jump`",
            inline=False,
        )
        page6.add_field(
            name=".sip",
            value="☕ Пить чаёк!\n `.sip`",
            inline=False,
        )
        page6.add_field(
            name=".yawn",
            value="🥱 Зевнуть!\n `.yawn`",
            inline=False,
        )
        page6.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page9 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по РП командам (2-й список) <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page9.add_field(
            name=".shrug",
            value="¯\_(ツ)_/¯ Что то не знает!\n `.shrug`",
            inline=False,
        )
        page9.add_field(
            name=".drink",
            value="🍻 Попить напиток!\n `.drink`",
            inline=False,
        )
        page9.add_field(
            name=".dab",
            value="😎 дэббить над хейтерами!\n `.dab`",
            inline=False,
        )
        page9.add_field(
            name=".nom",
            value="🌮 Голодеть!\n `.nom`",
            inline=False,
        )
        page9.add_field(
            name=".nosebleed",
            value="🩸 думает что это стрёмно! >.<\n `.nosebleed`",
            inline=False
        )
        page9.add_field(
            name=".run",
            value="🏃 Бежать куда-то!\n `.run`",
            inline=False,
        )
        page9.add_field(
            name=".sleep",
            value="😴 сладко спать :3\n `.sleep`",
            inline=False,
        )
        page9.add_field(
            name=".stare",
            value="👀 Всё видит!\n `.stare`",
            inline=False,
        )
        page9.add_field(
            name=".laugh",
            value="😂 Посмеяться!\n `.laugh`",
            inline=False,
        )
        page9.add_field(
            name=".yaoicuddle",
            value="👨👐👨 Прижиматся к пользователю в стиле яой!\n .yaoicuddle [пользователь] [комментарий]",
            inline=False,
        )
        page9.add_field(
            name=".yaoihug",
            value="👨👐👨 Обнимать пользователя в стиле яой!\n `.yaoihug [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".yuricuddle",
            value="👩👐👩 Прижиматся к пользователю в стиле юри!\n `.yuricuddle [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".yurihug",
            value="👩👐👩 Обнимать пользователя в стиле юри!\n `.yurihug [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".yaoikiss",
            value="👨‍❤️‍👨 Поцеловать пользователя в стиле яой!\n `.yaoikiss [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".yeet",
            value="💨 швырнуть пользователя!\n `.yeet [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".highfive",
            value="🤚 Дать пятюню пользователю!\n `.highfive [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".massage",
            value="💆 Сделать массаж пользователю!\n `.massage [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".marry",
            value="💍 Пожениться вместе с пользователем! >-<\n `.marry [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".merkel",
            value="🇩🇪 Меркельнуть пользователя!\n `.merkel [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".reward",
            value="🍓 Выдать награду пользователю в виде клубники!\n `.reward [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".squish",
            value="🍩 Потискать пользователя!\n `.squish [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".bonk",
            value="🏏 Дать бонк пользователю!\n `.bonk [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".yurikiss",
            value="👩‍❤️‍👩 Поцеловать пользователя в стиле юри!\n `.yurikiss [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".arrest",
            value="👮 Посадить пользователя в тюрму!\n `.arrest [пользователь] [комментарий]`",
            inline=False,
        )
        page9.add_field(
            name=".awkward",
            value="😅 Почувствовать себя не ловко uwu!\n `.awkward`",
            inline=False,
        )
        page9.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page11 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по РП командам (3-й список) <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page11.add_field(
            name=".ghoul",
            value="👻 Стать гулем!\n `.ghoul`",
            inline=False,
        )
        page11.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )
    
        page7 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по Админ командам <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page7.add_field(
            name=".embed",
            value="Написать через embed!\n`.embed название | описание` `",
            inline=False,
        )
        page7.add_field(
            name=".say",
            value="Написать через бота!\n `.say [текст]`",
            inline=False,
        )
        page7.add_field(
            name=".ping",
            value="Пингануть @everyone!\n `.ping`",
            inline=False,
        )
        page7.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        page8 = nextcord.Embed(
            title="Помощь по командам ➲",
            description="Помощь по РП 18+ <:Beta_1:1097196329597411478><:Beta_2:1097196351340683455><:Beta_3:1097196367341948968>, ❗ Внимание ❗ Вы должны использовать данные команды в канале где обозначен `18+` и другие участники должны согласны на просмотр данного контента! По правилам **Discord ToS**",
            timestamp=datetime.datetime.now(),
            color=nextcord.Color.blue(),
        )
        page8.add_field(
            name=".sixnine",
            value="👅💦 Делать 69 вместе с пользователем!\n `.sixnine [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".assfuck",
            value="🍆🍑 Трахать в попу пользователя!\n `.assfuck [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".assgrab",
            value="🍑👐 Полапать попку пользователя!\n `.assgrab [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".blowjob",
            value="🍆💦 Сделать минетик пользователю!\n `.blowjob [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".bondage",
            value="🪢 Заняться развратными бондажными штучками вместе с пользователям!\n `.bondage [пользватель] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".boobsgrab",
            value="🍒👐 Полапать грудь пользователя!\n `.boobsgrab [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".boobsuck",
            value="🍒👅 Пососать сиськи у пользователя!\n `.boobsuck [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".creampie",
            value="🍆💦 Кончить в пользователя!\n `.creampie [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".cum",
            value="💦👅 Кончить на пользователя!\n `.cum [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".dickride",
            value="🍆 Покататся на члене пользователя!\n `.dickride [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".facesit",
            value="🪑 Сесть на лицо пользователя!\n `.facesit [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".finger",
            value="👇 Воткнуть пальцем в пользователя!\n `.finger [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".footjob",
            value="🦶💦 Получить футджоб от пользователя!\n `.footjob [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".fuck",
            value="🍆🛏💦 Потрахатся с пользователем!\n `.fuck [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".furryfuck",
            value="🦊💦 Трахатся в стиле фурри вместе с пользователем\n `.furryfuck [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".handjob",
            value="🍆👅 Подрочить пользователю!\n `.handjob [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".leash",
            value="🦮 Надеть на себя поводок!\n `.leash`",
            inline=False,
        )
        page8.add_field(
            name=".masturbate",
            value="💦 Подрочить на пользователя!\n `.masturbate [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".pussyeat",
            value="👅💦 Полизать киску пользователя!\n `.pussyeat [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".spank",
            value="🍑 Шлёпать пользователя по попе!\n `.spank [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".strip",
            value="👙 станцевать стрип для участника!\n `.strip [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".tittyfuck",
            value="🥥 Трахать титьками пользователя!\n `.tittyfuck [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".yaoifuck",
            value="👨🛏👨️ трахать пользователя в стиле яой!\n `.yaoifuck [пользователь] [комментарий]`",
            inline=False,
        )
        page8.add_field(
            name=".yurifuck",
            value="👩🛏👩️ трахать пользователя в стиле юри!\n `.yurifuck [пользователь] [комментарий]`",
            inline=False,
        )
        page8.set_footer(
            text=interaction.user.name, icon_url=interaction.user.display_avatar
        )

        if self.values[0] == "Главное меню ➲":
            return await interaction.response.edit_message(embed=page1)
        elif self.values[0] == "Информация ➲":
            return await interaction.response.edit_message(embed=page2)
        elif self.values[0] == "Утилиты ➲":
            return await interaction.response.edit_message(embed=page3)
        elif self.values[0] == "Развлечения ➲":
            return await interaction.response.edit_message(embed=page4)
        elif self.values[0] == "Развлечения (continuation) ➲":
            return await interaction.response.edit_message(embed=page10)
        elif self.values[0] == "Модерация ➲":
            return await interaction.response.edit_message(embed=page5)
        elif self.values[0] == "RolePlay ➲":
            return await interaction.response.edit_message(embed=page6)
        elif self.values[0] == "RolePlay (continuation) ➲":
            return await interaction.response.edit_message(embed=page9)
        elif self.values[0] == "RolePlay (continue) ➲":
            return await interaction.response.edit_message(embed=page11)
        elif self.values[0] == "Административное ➲":
            return await interaction.response.edit_message(embed=page7)
        elif self.values[0] == "RolePlay 18+ ➲":
            return await interaction.response.edit_message(embed=page8)


class HelpCommandView(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(HelpCommand())
