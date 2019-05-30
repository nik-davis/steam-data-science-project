def export_data(df, filename, prefix='steam_', extension='.csv'):
    """Export dataframe to csv file, filename prepended with 'steam_'.
    
    filename : str without file extension
    """
    filepath = '../data/exports/' + prefix + filename + extension
    print_name = filename.replace('_', ' ')
    
    df.to_csv(filepath, index=False)
    
    print("Exported {} to '{}'".format(print_name, filepath))
    
    
def print_steam_links(df):
    """Print links to store page for apps in a dataframe."""
    url_base = "https://store.steampowered.com/app/"
    
    for i, row in df.iterrows():
        appid = row['steam_appid']
        name = row['name']
        
        print(name + ':', url_base + str(appid))