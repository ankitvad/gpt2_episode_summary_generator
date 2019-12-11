import os
import argparse


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Wikipedia episode summary parser.",
        formatter_class=lambda prog: argparse.RawTextHelpFormatter(prog, width=75)
    )
    parser.add_argument('-s', '--start_url', type=str, required=True,
                        help='start URL for the spider.'
                             '\nShould be: '
                             'https://en.wikipedia.org/wiki/<Show_Title_With_Underscores_And_Capitalized_Init_Chars>'
                             '\nExample: https://en.wikipedia.org/wiki/Star_Trek')
    parser.add_argument('-a', '--allow', type=str, required=True,
                        help='Wikipedia urls must include this substring otherwise the spider will not enter the URL.'
                             '\nIdeally, it should be: <Show_Title_With_Underscores_And_Capitalized_Init_Chars>'
                             '\nExample: \"Star_Trek\"')
    parser.add_argument('-d', '--deny', type=str, required=False, default=None,
                        help='The Wikiepdia spider will NOT examine the pages which contain '
                             'any of these substrings in their urls.')
    parser.add_argument('-t', '--title_keywords', nargs='*', required=False, default='',
                        help='The title of the Wikipedia page must include these keywords, '
                             'otherwise the spider will not extract anything from the page.'
                             '\n Good practice: use the lowercase version of the words from the show\'s title'
                             '\n Example: Star Trek')
    parser.add_argument('-o', '--output_path', type=str, required=False, default='wiki_episode_summaries.json',
                        help='Path to the output JSON file.')

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_arguments()

    call = 'scrapy crawl wiki_episode_table_spider -a start_url=\"{}\" -a allow=\"{}\" -a deny=\"{}\" ' \
           '-a title_keywords=\"{}\" -o {}'.format(args.start_url,
                                                   args.allow,
                                                   args.deny,
                                                   ' '.join(args.title_keywords),
                                                   args.output_path)
    os.system(call)