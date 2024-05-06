from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import random

# Dictionary for different color themes
color_themes = {
    0: ['#FFD700', '#8B4513', '#FFA500'],  # Yellow, Brown, Orange
    1: ['#228B22', '#ADFF2F', '#006400'],  # Green, Light Green, Dark Green
    2: ['#A9A9A9', '#000000', '#708090'],  # Gray, Black, Dark Blue Gray
    3: ['#FF0000', '#FFA07A', '#DC143C'],  # Red, Light Red, Crimson
    4: ['#A52A2A', '#B8860B', '#D2B48C'],  # Brown, Burnt Brown, Light Brown
    5: ['#FFC0CB', '#FF69B4', '#FFDAB9'],  # Pink, Rose, Peach
    6: ['#ADD8E6', '#0000FF', '#9370DB'],  # Light Blue, Blue, Light Purple
    7: ['#00008B', '#800080', '#000435']  # Dark Blue, Purple
}


def generate_color_func(theme_colors):
    """
    Generates a color function that returns a color based on the specified theme.

    :param theme_colors: List of theme colors to use for the word cloud.
    :return: Function that returns a color.
    """
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        weights = [0.4, 0.3, 0.3]  # Higher probability for the first color
        return random.choices(theme_colors, weights=weights, k=1)[0]

    return color_func

def generate_slogan_wordcloud_with_theme(slogans, output_path, theme_index):
    """
    Generates a word cloud from a list of slogans with a specific color theme and saves it to the specified file path.

    :param slogans: List of slogan strings
    :param output_path: Path to save the generated word cloud image
    :param theme_index: Index from 0 to 7 representing the desired color theme
    """
    if theme_index not in color_themes:
        raise ValueError("Invalid theme index. Choose a number from 0 to 7.")

    # Customize frequencies for more variation in size
    slogan_frequencies = {slogan: len(slogan) for slogan in slogans}

    # Create the word cloud with explicit settings
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path='fonts/Nabi.ttf',
        prefer_horizontal=0.5,
        scale=2,
        random_state=None,
        relative_scaling=1,
        stopwords=STOPWORDS,
        color_func=generate_color_func(color_themes[theme_index])
    ).generate_from_frequencies(slogan_frequencies)

    # Display and save the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.savefig(output_path)
    plt.close()

# Example usage:
slogans = [
    'حفظ آسایش دهان با خمیردندان حاوی فلوراید',
    'سفید کننده دندان برای اطمینان شما',
    'خمیردندان با فلوراید برای احتیاط دندان',
    'سادگی و آسایش با خمیردندان حاوی فلوراید',
    'خمیردندان سفید کننده برای اطمینان شما',
    'آسایش و احتیاط با خمیردندان حاوی فلوراید',
    'خمیردندان برای دندان های سفید و آسایش',
    'فلوراید برای اطمینان از سلامت دهان',
    'خمیردندان حاوی فلوراید برای آسایش دهان',
    'طعم اصیل لبنیات با پنیر طبیعی',
    'لذت ببر با هر برش پنیر',
    'پنیر تازه، طعم سلامت',
    'شروع صبح با طعم دل‌نشین پنیر',
    'بهترین همراه سفره صبحانه، پنیر',
    'سلامت و انرژی در هر لقمه پنیر',
    'پنیر؛ غذای سالم برای همه سنین',
    'طراوت و طعم در هر لقمه از پنیر',
    'پنیر با عشق درست شده است',
    'پنیر، تجربه طعم اصیل لبنیات',
    'پنیر، هم‌نشین دائمی سفره‌ها',
    'طراوت و تازگی پنیر در هر لقمه',
    'هر لقمه پنیر، طعمی دل‌نشین',
    'یک لقمه پنیر، سلامتی به همراه',
    'بهترین انتخاب برای طعم عالی، پنیر',
    'پنیر طبیعی، همواره طعم عالی',
    'بهترین طعم و تازگی در پنیر طبیعی',
    'با پنیر، لبخند به روزتان بزنید',
    'شروع هر روز با پنیر تازه و سالم',
    'سفید کننده دندان برای احتیاط و اطمینان'
]

output_path = 'wordcloud_slogans_with_theme.png'
theme_index = 7  # Change to the desired theme index (0 to 7)
generate_slogan_wordcloud_with_theme(slogans, output_path, theme_index)
