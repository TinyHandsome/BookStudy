# VERSION: 1.0
# AUTHOR: jac

from helpers import retrieve_url
from novaprinter import prettyPrinter
import re


class horriblesubs(object):
    """
    Required Static Variables
    -------------------------
    url : str
         The url of the search engine
    name : str 
        Name of the search engine
    supported_categories : dict
        Supported QBittorrent categories
    """

    url = "https://horriblesubs.info"
    name = "HorribleSubs"
    supported_categories = {"all": "0", "anime": "7"}

    def __init__(self):
        pass

    def download_torrent(self, download_url):
        """
        Magnet links and .torrent files only available from a show's page
        This calls a relevant function to retieve magnet link

        Parameters
        ----------
        download_url : str
            `link` in dictionary passed to self.torrent_dict in search method
        """
        download_split = download_url.split("#")
        show_page = retrieve_url(download_split[0])
        episode_number = download_split[1]
        quality = download_split[2]
        url = "/api.php?method=getshows&type={0}&showid=" \
            .format("batch" if "-" in episode_number else "show")

        # Append show id to url
        url += re.search("_s.+ (.+?);", show_page).group(1)
        # 12 most recent episodes/batches
        recent = retrieve_url(self.url + url)

        # Get page number which contains desired torrent
        if "type=show" in url:
            episode_number = int(episode_number)
            # Episode number of most recent episode
            most_recent = int(re.search("r.{22}\"(.+?)\"", recent).group(1))
            # Check if not in most recent 12
            if most_recent - 11 > episode_number:
                # Retrieve page which contains episode
                page_num = (most_recent - episode_number) // 12
                url += "&nextid={0}".format(page_num)
        else:
            pass
        page = retrieve_url(self.url + url)
        re_query = "{0}-{1}.+?f=\"(.+?)\"".format(episode_number, quality)
        magnet_link = re.search(re_query, page).group(1)
        print(magnet_link + " " + magnet_link)

    def search(self, query, cat="all"):
        """
        Function called by QBittorrent to do searching
        DO NOT CHANGE name of function or parameters

        Parameters
        ----------
        query : str
            Escaped search query
        cat : str
            Name of category to search
        """
        # API returns up to 6 pages
        for page_num in range(6):
            url = "/api.php?method=search&value={0}&nextid={1}" \
                .format(query, page_num)
            response = retrieve_url(self.url + url)
            # Stop iteration if there are no more pages of results
            if response == "Nothing was found":
                break

            # Split html into each episode
            torrents = re.sub("<d.{17}s.+?v>", "", response).split("</li>")
            # For raw html of each episode. [:-1] ignores "</ul>" at list end
            for html in torrents[:-1]:
                # Get the name of the episode
                generic_name = re.search("n>(.+?)</st", html).group(1) \
                    .replace("<strong>", "")
                # Link to show page w/ episode number i.e link#01
                show_and_ep = re.search("f=\"(.+?)\"", html).group(1)
                # For each quality the episode is available in
                for quality_match in re.finditer("ge\">(.+?)<", html):
                    # Change SD to 480p
                    quality = quality_match.group(1)
                    quality = "480p" if quality == "SD" else quality
                    # Create search result
                    name = generic_name + " [" + quality + "]"
                    link = self.url + show_and_ep + \
                        "#" + quality
                    desc = self.url + show_and_ep.split("#")[0]
                    episode = self.torrent_dict(name, link, desc)
                    prettyPrinter(episode)

    def torrent_dict(self, name, link, desc_link):
        """
        Returns a dictionary used by QBittorrent to display search result

        Parameters
        ----------
        name : str
            Name of the torrent
        link : str
            Download URL
        desc_link : str
            URL to torrent description

        Returns
        -------
        dict
            A dict containing default entries used by Qbittorrent per result.
            Value of "-1" means the value is unknown. HorribleSubs does not
            track seeds/leechers/size on their site.
        """
        return {"name": name, "seeds": "-1", "leech": "-1", "size": "-1",
                "link": link, "desc_link": desc_link, "engine_url": self.url}


# Debug testing code
if __name__ == "__main__":
    debug = horriblesubs()
    debug.search("kenja+no+mago")
    # debug.download_torrent(
    #     "https://horriblesubs.info/shows/kenja-no-mago#03#720p")
