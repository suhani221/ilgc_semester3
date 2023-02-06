import pandas as pd
import folium
import branca
import os

path = "/Users/suhaniagarwal/Desktop/ilgc_website_2/Map Maker/Punjab_HWC_Data/"
dir_list = os.listdir(path)
dir_list.sort()
print(dir_list)
for file in dir_list:
    df = pd.read_csv(path+file)
    df.columns = df.columns.str.strip()
    # print(df)
    latitude = df.loc[1]['Latitude']
    longitude = df.loc[1]['Longitude']
    map = folium.Map(location=[latitude, longitude], zoom_start=12)


    def popup_html(row):
        i = row
        breastcancer=df['breastcancer'].iloc[i] 
        diabetes=df['diabetes'].iloc[i]
        footfall = df['footfall'].iloc[i] 
        hypertension=df['Hypertension'].iloc[i] 
        Oralcancer = df['Oralcancer'].iloc[i]
        Latitude = df['Latitude'].iloc[i]
        Longitude = df['Longitude'].iloc[i]
        Block_Name = df['HFI'].iloc[i]
        Hyper_Link = df['Hyper Link'].iloc[i]

        left_col_color = "#f0f0f0"
        right_col_color = "#edbf33"

        x= '<a href="https://www.google.com/maps?q='+str(Latitude)+","+str(Longitude)+'" target="_blank style="text-decoration: none;color:black;">Open in Google Maps</a>'

        HWC_Link = '<a href="'+str(Hyper_Link)+'"'+' target="_blank" style="text-decoration: none;color:red;" >'+ str(Block_Name) + '</a>'
        html = """<!DOCTYPE html>
    <html>

    <head>
    <h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(HWC_Link) + """

    </head>
        <table style="height: 160px; width: 420px;">
    <tbody>

    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Latitude</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Latitude) + """
    </tr>

    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Google Location</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(x) + """
    </tr>

    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: black;">Longitude</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Longitude) + """
    </tr>


    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Footfall</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(footfall) + """
    </tr>

    <tr>
    <td style="background-color: """+ left_col_color +""";">
    <span style="color: black;">Breastcancer</span>
    </td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(breastcancer) + """
    </tr>


    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Diabetes</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(diabetes) + """
    </tr>

    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Hypertension</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(hypertension) + """
    </tr>

    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Oral Cancer</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Oralcancer) + """
    </tr>

    </tbody>
    </table>
    </html>
    """
        return html

    incidents = folium.map.FeatureGroup()
    control_scale=True
    zoom_start=14
    for lat, lng, cat in zip(df.Latitude, df.Longitude, df.Category):
        if (cat == 'UPHC'):
            incidents.add_child(
            folium.Circle(
            [lat, lng],
            radius=float(2000), 
            color="red",
            opacity=0.0,
            fill=True,
            fill_color='red',
            fill_opacity=0.0 ))
        if (cat == 'PHC'):
            incidents.add_child(
            folium.Circle(
            [lat, lng],
            radius=float(2000), 
            color="blue",
            opacity=0.1,
            fill=True,
            fill_color='blue',
            fill_opacity=0.1 ))
        if (cat == 'SHC'):
            incidents.add_child(
            folium.Circle(
            [lat, lng],
            radius=float(2000), 
            color="green",
            fill=True,
            opacity=0.0,
            fill_color='green',
            fill_opacity=0.1 ))

    for i in range(0,len(df)):
        html = popup_html(i)
        iframe = branca.element.IFrame(html=html,width=510,height=280)
        popup = folium.Popup(folium.Html(html, script=True), max_width=500)
        if (df['Category'].iloc[i] == 'UPHC'):
            folium.Marker([df['Latitude'].iloc[i],df['Longitude'].iloc[i]],
            popup=popup,icon=folium.Icon(color="red", icon="plus", prefix='fa')).add_to(map)
        if (df['Category'].iloc[i] == 'SHC'):
            folium.Marker([df['Latitude'].iloc[i],df['Longitude'].iloc[i]],
            popup=popup,icon=folium.Icon(color="green", icon="plus", prefix='fa')).add_to(map)
        if (df['Category'].iloc[i] == 'PHC'):
            folium.Marker([df['Latitude'].iloc[i],df['Longitude'].iloc[i]],
            popup=popup,icon=folium.Icon(color="blue", icon="plus", prefix='fa')).add_to(map)  
    
        map.add_child(incidents)
    
    incidents.save("/Users/suhaniagarwal/Desktop/ilgc_website_2/Map Maker/Maps/"  + file.split('.')[0] + '.html')
    print("Map Generated for --> " + file.split('.')[0])
