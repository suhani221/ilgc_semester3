import pandas as pd
import numpy as np
from math import radians, cos, sin, asin, sqrt
import pandas as pd
import folium
import branca

def make_map_pincode(pincode):
    df= pd.read_csv('/Users/suhaniagarwal/Desktop/ILgc/ilgc_website_2/ilgc_website/INDIA_LAT_LONG.csv')
    df["pincode"]=df["key"].str.split("/").str.get(1)


    def search(pincode):
        pincode = str(pincode)
        for index, row in df.iterrows():
            if row['pincode'] == pincode:
                lati1=row["latitude"]
                loni2=row["longitude"]
                return(lati1,loni2)
                break
        else:
            print("not found")

    lati1,loni1=search(pincode)

    data = pd.read_csv('/Users/suhaniagarwal/Desktop/ILgc/ilgc_website_2/Map Maker/Punjab_HWC_Data/combined.csv')
    r = 6371
    data_query=pd.DataFrame()
    for i in range(len(data)):
        lat2=data.loc[i, "Latitude"]
        lon2=data.loc[i, "Longitude"]
        lon1 = radians(loni1)
        lon2 = radians(lon2)
        lat1 = radians(lati1)
        lat2 = radians(lat2)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * asin(sqrt(a))
        if(c*r<=2):
            data_query=data_query.append(data.loc[i])
    print(data_query)

            # data_query=data_query.append(data.loc[i])


    def popup_html(row):
        i = row
        breastcancer=data_query['breastcancer'].iloc[i] 
        diabetes=data_query['diabetes'].iloc[i]
        footfall = data_query['footfall'].iloc[i] 
        hypertensioon=data_query['Hypertension'].iloc[i] 
        Oralcancer = data_query[' Oralcancer '].iloc[i]
        Latitude = data_query['Latitude'].iloc[i]
        Longitude = data_query['Longitude'].iloc[i]
        Block_Name = data_query['HFI'].iloc[i]

        left_col_color = "#f2f0d3"
        right_col_color = "#f2f0d3"
        black="#000000"
        
        
        html = """<!DOCTYPE html>
    <html>

    <head>
    <h4 style="margin-bottom:10"; width="200px">{}</h4>""".format(Block_Name) + """

    </head>
        <table style="height: 126px; width: 350px;">
    <tbody>

    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Latitude</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Latitude) + """
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
    <span style="color: black;">breastcancer</span>
    </td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(breastcancer) + """
    </tr>


    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Diabetes</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(diabetes) + """
    </tr>

    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Hypertensioon</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(hypertensioon) + """
    </tr>

    <tr>
    <td style="background-color: """+ left_col_color +""";"><span style="color: #000000;">Oralcancer</span></td>
    <td style="width: 150px;background-color: """+ right_col_color +""";">{}</td>""".format(Oralcancer) + """
    </tr>

    </tbody>
    </table>
    </html>
    """
        return html

    map = folium.Map(location=[lati1, loni1], zoom_start=12)
    folium.Marker(location=[lati1, loni1], popup="You are here", icon=folium.Icon(color="green", icon="info-sign")).add_to(map)
    folium.Circle(location=[lati1, loni1], radius=2000, weight=1, color="#000").add_to(map)


    incidents = folium.map.FeatureGroup()
    control_scale=True
    zoom_start=14
    for lat, lng, cat in zip(data_query.Latitude, data_query.Longitude, data_query.Category):
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

        for i in range(0,len(data_query)):
            html = popup_html(i)
            iframe = branca.element.IFrame(html=html,width=510,height=280)
            popup = folium.Popup(folium.Html(html, script=True), max_width=500)
            if (data_query['Category'].iloc[i] == 'UPHC'):
                folium.Marker([data_query['Latitude'].iloc[i],data_query['Longitude'].iloc[i]],
                popup=popup,icon=folium.Icon(color="red", icon="plus", prefix='fa')).add_to(map)
            if (data_query['Category'].iloc[i] == 'SHC'):
                folium.Marker([data_query['Latitude'].iloc[i],data_query['Longitude'].iloc[i]],
                popup=popup,icon=folium.Icon(color="green", icon="plus", prefix='fa')).add_to(map)
            if (data_query['Category'].iloc[i] == 'PHC'):
                folium.Marker([data_query['Latitude'].iloc[i],data_query['Longitude'].iloc[i]],
                popup=popup,icon=folium.Icon(color="blue", icon="plus", prefix='fa')).add_to(map)  
        
            map.add_child(incidents)

    map.save("templates/generated.html")
