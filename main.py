from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.clipboard import Clipboard
from kivy.storage.jsonstore import JsonStore
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window


# =========================
# MOBILE MODE
# =========================
Window.size = (360, 640)


# =========================
# STORAGE
# =========================
store = JsonStore("favorites.json")


# =========================
# DATA
# =========================
banners = [
    {
        "image": "1489.jpg",
        "title": "Gaming Banner",
        "category": "Gaming",
        "tags": ["neon", "dark"],
        "prompt": "A professional YouTube gaming banner with a dark charcoal grey background. In the center, large bold futuristic typography that says 'FARHAN GAMER' in glowing neon green text. Below the text, a square frame with a neon green glow for a profile photo. At the bottom, clean icons for 'Subscribe', 'Like', and 'Comment' inside rounded glassmorphism buttons. High-quality 8k resolution, cinematic lighting, sleek gaming aesthetic. AI generated"
    },
    {
        "image": "1498.jpg",
        "title": "YouTube Banner",
        "category": "YouTube",
        "tags": ["clean", "modern"],
        "prompt": "A professional YouTube gaming banner with a dark textured navy blue background. On the left side, a sleek rectangular frame with a subtle glow that says 'Your Photo Here'. In the center-right, large bold 3D silver typography saying 'FARHAN GAMER'. The design features sharp horizontal neon light streaks in cyan blue on the left and vibrant purple on the right. At the bottom center, a red 'Subscribe' button followed by white 'Like', 'Comment', and notification bell icons. High-quality 8k, cinematic gaming aesthetic, sharp details"
    },
    {
        "image": "1494.jpg",
        "title": "Instagram Banner",
        "category": "Instagram",
        "tags": ["aesthetic", "soft"],
        "prompt": "An epic professional YouTube gaming banner with a dark, textured stone wall background. At the top, bold 3D golden metallic text saying 'FARHAN GAMER' with a glowing orange outline. In the center, a majestic golden shield-shaped emblem frame with a bright orange neon glow and the text 'Your Photo Here' inside. The scene is filled with realistic flying fire sparks and embers. At the bottom, a heavy metallic bronze console bar containing 'Subscribe', 'Like', 'Comment', and 'Notifications' icons. Cinematic 8k resolution, high contrast, dramatic lighting."
    },
    {   "image": "1490.jpg",
        "title": "Ultra Cinematic Gaming War Zone Banner",
        "category": "Gaming",
        "tags": ["neon", "dark"],
        "prompt": "A high-tech professional YouTube gaming banner with a dark blue futuristic background featuring glowing circuit board patterns and digital lines. In the center, bold white typography with a bright cyan neon glow saying 'FARHAN GAMER'. Below the main text, a sleek rectangular frame with a blue neon outline for a profile photo. On the bottom, a vibrant red 'Subscribe' button alongside blue glowing 'Like', 'Comment', and 'Notifications' icons. The overall aesthetic is sci-fi, cyberpunk, and ultra-modern with cinematic lighting and 8k resolution."
    },
    {   
        "image": "1491.jpg",
        "title": "Cyber Neon Esports Arena Banner",
        "category": "YouTube",
        "tags": ["neon", "dark"],
        "prompt": "A professional YouTube gaming banner with a deep black and dark purple tech background. The design features glowing purple circuit board patterns and digital lines with floating particles. In the center, the name 'FARHAN GAMER' is written in a bold, futuristic font with a purple-to-blue gradient glow. Below the name, a rounded rectangular frame with a bright purple neon outline for a profile picture. At the bottom, a stylish 'Subscribe' button and minimalist icons for Like, Comment, and Notifications, all glowing in purple. High-tech cyberpunk aesthetic, 8k resolution, cinematic lighting, sleek and modern."
    },
    {   
        "image": "1492.jpg",
        "title": "Futuristic Tech YouTube Channel Banner",
        "category": "Instagram",
        "tags": ["neon", "dark"],
        "prompt": "A professional YouTube gaming banner with a dark stone-textured background integrated with glowing orange lava circuit board patterns. In the center, the text 'FARHAN GAMER' is written in a heavy, 3D rock-style font with a bright orange fire-glow effect. Below the name, a rectangular frame with a jagged lightning-style orange neon outline for a photo. The scene is decorated with flying fire embers and floating black geometric rocks. At the bottom, a sleek dark console bar with an orange 'Subscribe' button and glowing orange icons for Like, Comment, and Notifications. Dramatic lighting, 8k resolution, cinematic gaming aesthetic."
    },
    {
        "image": "1493.jpg",
        "title": "Dark Mode Pro Gaming Stream Overlay Banner",
        "category": "Gaming",
        "tags": ["neon", "dark"],
        "prompt": "A highly detailed, epic YouTube gaming banner with a dark metallic stone background covered in glowing orange circuit board paths and microchip details. At the top, bold 3D text 'FARHAN GAMER' made of forged molten iron with internal orange fire-glow. In the center, a large, intricate cybernetic shield emblem with glowing orange vines and mechanical parts, containing the text 'Your Photo Here'. On the bottom corners, two massive futuristic mechanical power-cubes (reactors) glowing with intense heat and smoke. At the bottom center, a heavy bronze metallic bar with 'Subscribe', 'Like', and 'Notifications' icons. The scene is filled with realistic fire embers, smoke effects, and cinematic lighting, 8k resolution, ultra-realistic gaming aesthetic."
    },
    {
        "image": "1495.jpg",
        "title": "High Detail Anime Style Gaming Banner",
        "category": "YouTube",
        "tags": ["neon", "dark"],
        "prompt": "A sleek and minimalist YouTube gaming banner with a clean, light grey and white gradient background. On the left side, large bold 3D white typography saying 'FARHAN GAMER' with a subtle soft shadow. On the right side, a square glassmorphism-style photo frame with a thin white glowing border. The entire design is framed by a delicate neon light border in soft orange and white. At the bottom right, simple and clean minimalist text icons for 'Subscribe', 'Like', and 'Comment'. High-quality 8k resolution, bright airy lighting, modern tech aesthetic, ultra-clean design."
    },
    {
        "image": "1499.jpg",
        "title": "Neon Cyberpunk Social Media Branding Banner",
        "category": "Instagram",
        "tags": ["neon", "dark"],
        "prompt": "A professional YouTube gaming banner with a dark grainy textured background. On the left side, bold 3D typography for the name 'FARHAN GAMER' featuring a vibrant gradient glow of electric blue and hot pink. To the right, a rectangular frame with a glowing dual-tone neon border (blue on top, pink on bottom) for a profile photo. At the bottom, clean UI buttons including a red 'Subscribe' button and white minimalist icons for 'Like', 'Comment', and a 'Notification Bell'. High-quality 8k resolution, cinematic neon lighting, vaporwave gaming aesthetic, sharp details."
    },
    {
        "image": "1500.jpg",
        "title": "Elite Tournament Esports Championship Banner",
        "category": "Gaming",
        "tags": ["neon", "dark"],
        "prompt": "A professional YouTube gaming banner with a dark cosmic background featuring subtle stars. On the left, bold 3D typography for the name 'FARHAN GAMER' with a vibrant cyan-to-pink gradient glow. The scene is energized with sharp diagonal light streaks in electric blue and hot pink. To the right, a sleek rectangular frame with an intense pink and blue neon glow for a profile photo. At the bottom, a red 'Subscribe' button with white minimalist 'Like', 'Comment', and 'Bell' icons. 8k resolution, cinematic lighting, high contrast, vibrant gaming aesthetic."
    },
    {
        "image": "banner1.jpg",
        "title": "Minimalist Modern Creator Branding Banner",
        "category": "YouTube",
        "tags": ["neon", "dark"],
        "prompt": "A professional YouTube gaming banner with a dark navy blue textured background. The design features two sharp horizontal neon light streaks: a bright cyan blue line on the left and a vibrant hot pink line on the right. In the center, the name 'FARHAN GAMER' is written in a bold, modern sans-serif font with a glowing blue-to-pink gradient. To the left of the name, a clean square frame with a subtle glow for a profile photo. At the bottom, a red 'Subscribe' button with minimalist white icons for 'Like', 'Comment', and 'Bell'. High-quality 8k, cinematic lighting, ultra-clean neon aesthetic."
    },
    {   
        "image": "YouTube.jpg",
        "title": "Holographic Glow Instagram Aesthetic Banner",
        "category": "Instagram",
        "tags": ["neon", "dark"],
        "prompt": "A professional YouTube gaming banner with a dark charcoal grey background. In the center, the name 'FARHAN GAMER' is written in a sleek, futuristic sci-fi font with a bright cyan neon glow. The design features sharp, angular cyan neon geometric lines that look like a tech HUD. Below the text, a small square glowing frame for a profile photo. At the bottom, clean rounded buttons for 'Subscribe', 'Like', and 'Comment' alongside a notification bell icon. High-quality 8k, minimalist tech aesthetic, sharp lighting, cinematic finish."
    },
    {   

        "image": "1",
        "title": "Ultra HD Motion Style Gaming Profile Banner",
        "category": "Gaming",
        "tags": ["neon", "dark"],
        "prompt": "Ultra HD gaming banner, neon cinematic style"
    },
    {   

        "image": "1",
        "title": "Gaming Banner",
        "category": "youtube",
        "tags": ["neon", "dark"],
        "prompt": "Ultra HD gaming banner, neon cinematic style"
    },
    {

        "image": "1",
        "title": "Gaming Banner",
        "category": "instagarm",
        "tags": ["neon", "dark"],
        "prompt": "Ultra HD gaming banner, neon cinematic style"
    },
    {   

        "image": "1",
        "title": "Gaming Banner",
        "category": "Gaming",
        "tags": ["neon", "dark"],
        "prompt": "Ultra HD gaming banner, neon cinematic style"
    },
    {

        "image": "1",
        "title": "Gaming Banner",
        "category": "youtube",
        "tags": ["neon", "dark"],
        "prompt": "Ultra HD gaming banner, neon cinematic style"
    },
    {   

        "image": "1",
        "title": "Gaming Banner",
        "category": "instagram",
        "tags": ["neon", "dark"],
        "prompt": "Ultra HD gaming banner, neon cinematic style"
    },
    {

        "image": "1",
        "title": "Gaming Banner",
        "category": "Gaming",
        "tags": ["neon", "dark"],
        "prompt": "Ultra HD gaming banner, neon cinematic style"

    }
]


# =========================
# PROMPT BOOST
# =========================
def boost(prompt, tags):
    return f"{prompt}, {', '.join(tags)}, 4K, cinematic, ultra realistic"


# =========================
# BANNER CARD
# =========================
class BannerCard(BoxLayout):

    def __init__(self, banner, **kwargs):
        super().__init__(orientation='vertical', size_hint_y=None, height=320, **kwargs)

        self.banner = banner
        self.final_prompt = boost(banner["prompt"], banner["tags"])

        self.img = AsyncImage(source=banner["image"], size_hint=(1, 0.6))
        self.add_widget(self.img)

        self.title = Label(text=banner["title"], size_hint=(1, 0.1))
        self.add_widget(self.title)

        self.prompt = Label(text=self.final_prompt, size_hint=(1, 0.2), font_size=11)
        self.add_widget(self.prompt)

        btns = BoxLayout(size_hint=(1, 0.1))

        copy = Button(text="Copy")
        fav = Button(text="❤️ Fav")

        copy.bind(on_press=self.copy_prompt)
        fav.bind(on_press=self.save_fav)

        btns.add_widget(copy)
        btns.add_widget(fav)

        self.add_widget(btns)

    def copy_prompt(self, instance):
        Clipboard.copy(self.final_prompt)
        instance.text = "Copied"

    def save_fav(self, instance):
        store.put(self.banner["title"], data=self.banner)
        instance.text = "Saved"


# =========================
# LIST VIEW
# =========================
class BannerList(BoxLayout):

    def __init__(self, data, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        scroll = ScrollView()
        self.container = BoxLayout(orientation='vertical', size_hint_y=None, spacing=10)
        self.container.bind(minimum_height=self.container.setter('height'))

        scroll.add_widget(self.container)
        self.add_widget(scroll)

        self.load(data)

    def load(self, data):
        self.container.clear_widgets()
        for b in data:
            self.container.add_widget(BannerCard(b))


# =========================
# HOME SCREEN
# =========================
class HomeScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        main = BoxLayout(orientation='vertical')

        self.search = TextInput(hint_text="Search banners...", size_hint=(1, 0.1))
        self.search.bind(text=self.search_filter)

        cat = BoxLayout(size_hint=(1, 0.1))
        for c in ["All", "Gaming", "YouTube", "Instagram"]:
            b = Button(text=c)
            b.bind(on_press=self.filter_cat)
            cat.add_widget(b)

        self.list_view = BannerList(banners)

        fav_btn = Button(text="Go to Favorites", size_hint=(1, 0.1))
        fav_btn.bind(on_press=lambda x: setattr(self.manager, "current", "fav"))

        main.add_widget(self.search)
        main.add_widget(cat)
        main.add_widget(self.list_view)
        main.add_widget(fav_btn)

        self.add_widget(main)

    def search_filter(self, instance, text):
        text = text.lower().strip()
        if text == "":
            self.list_view.load(banners)
        else:
            self.list_view.load([b for b in banners if text in b["title"].lower()])

    def filter_cat(self, instance):
        if instance.text == "All":
            self.list_view.load(banners)
        else:
            self.list_view.load([b for b in banners if b["category"] == instance.text])


# =========================
# FAVORITES SCREEN
# =========================
class FavScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')

        self.list_view = BannerList([])

        back = Button(text="Back", size_hint=(1, 0.1))
        back.bind(on_press=lambda x: setattr(self.manager, "current", "home"))

        layout.add_widget(self.list_view)
        layout.add_widget(back)

        self.add_widget(layout)

    def on_enter(self):
        data = []
        for k in store.keys():
            try:
                data.append(store.get(k)["data"])
            except:
                pass
        self.list_view.load(data)


# =========================
# APP (SCREEN MANAGER FIXED)
# =========================
class BannerApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(FavScreen(name="fav"))
        return sm


BannerApp().run()

