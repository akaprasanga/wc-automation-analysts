#importing general objects
import pandas as pd
import plotly.express as px
import streamlit as st


st.title('Global Pollution Analyzation')

st.header('The masterminds behind this project')

st.write("Suniti Srinivasan:: Hi, I'm Suniti and I am a freshman at Internatinoal Community School. In my free time I enjoy rock climbing, dancing, and writing.")
st.write("Tony Tran:: Hi, I'm Tony and I'm a freshmen at Sheldon Highschool in California. My hobbies/interests are whittling, running, and basketball.")
st.write("Jeffrey MacLeod:: Hello my name is Jeffrey. I live in Canada on Vancouver Island; I go to Spectrumm high school and am currently in grade 10. I enjoy moutian biking, rock climbling and any activity outside.")
st.write("Lucas Cable:: I'm Lucas - a freshman at Early College High School in California. Some of my hobbies/interests include playing the drums, Table Tennis, and anything math related.")

#description: Our dataset will be about Global Pollution and it's contributors, individual factors, and comparisons between the two.

st.markdown("""---""")
my_dataset = pd.read_csv("Cleaned_Global_pollution.csv")

#show off a bit of your data.
st.header('Our Data')
st.write("Our dataset will be about Global Pollution and it's contributors, individual factors, and comparisons between the two. In our original dataset we had a lot of NULL and missing values. In order to solve that issue we dropped all the columns that had more than 40% of missing values. After that, we used Median and Mode Imputation techniques to fill the missing values. And below is our cleaned dataset.")
st.write(my_dataset)
st.markdown("""---""")

st.header('How much waste does each country produce')
st.write('How much do countries total waste percentages vary?')
fig = px.bar(my_dataset, x = "country_name", y = ['total_msw_total_msw_generated_tons_year'], title = "Countries total waste").update_layout(
    xaxis_title="Countries", yaxis_title="Waste Generated in a Year (tons)"
)

fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
newnames = {'total_msw_total_msw_generated_tons_year':'Waste Generated in a Year (tons)'}
fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )
                  
st.plotly_chart(fig)
st.write("We can see from this data that China, the United States, and India have the highest waste percentages, each in the range of 400-100 million tons of waste annually")

st.markdown("""---""")

########### Jefferey's plot

st.header("Country with highest composition of plastic")

fig = px.bar(my_dataset, y='composition_plastic_percent', x='country_name', color ="region_id")
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig)
st.write('In conclusion the country that produces the most amount of composition plastic is Palau. Palau is part of the region EAS.')

st.markdown("""---""")

########### Jeffrey's plot #2

st.header("Which region has the highest compostion of plastic")

fig = px.bar(my_dataset, y='composition_plastic_percent', x='region_id', color ="region_id", hover_data = ['country_name'])
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'}, title = 'Which region has the highest compostion of plastic')

st.plotly_chart(fig)
st.write('The Region that produces the most amount of composition plastic is ECS. The ECS includes the following countries Austria, Belgium, Czech Republic, Denmark, Estonia, Finland, France, Germany, Greece, Hungary, Ireland, Italy, Luxembourg, the Netherlands, Norway, Poland, Portugal, Romania, Spain, Sweden, Switzerland and the United Kingdom.')

st.markdown("""---""")


st.header('Which waste is more common?')
st.write("Glass waste and metal waste aren't necessarily the easiest wastes to come by but which one is more common? I personally think glass would be more common.")
fig = px.bar(my_dataset, x = "country_name", y = ["composition_glass_percent", "composition_metal_percent"], title = "Metal to Glass Waste Percentage", color_discrete_map={"composition_glass_percent":"cornflowerblue", "composition_metal_percent":"crimson"})
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
newnames = {'composition_glass_percent':'Glass Percentage', 'composition_metal_percent': 'Metal Percentage'}

fig.for_each_trace(lambda t: t.update(name = newnames[t.name],
                                      legendgroup = newnames[t.name],
                                      hovertemplate = t.hovertemplate.replace(t.name, newnames[t.name])
                                     )
                  )
st.plotly_chart(fig)
st.write("In conclusion, glass waste is more common than metal waste among most countries.")

st.markdown("""---""")
         
st.header('How does the composition rate of a country affect its population')
st.write('How does a countries organic waste percent affect its population')
my_dataset_text = my_dataset[['population_population_number_of_people', 'composition_food_organic_waste_percent']]
countries = ["Aruba", "Afghanistan", "Angola", "Albania", "Andorra", "Kosovo", "Yemen, Rep.", "South Africa", "Zambia", "Zimbabwe"]
n_countries = len(countries)

# Save months and seasons to new dataframe
column_1= my_dataset_text["population_population_number_of_people"]
column_2= my_dataset_text["composition_food_organic_waste_percent"]
# Use column names of df for the different parameters x, y, color, ...
fig = px.scatter(my_dataset_text, x="composition_food_organic_waste_percent", y="population_population_number_of_people",
                 title="composition food organic waste percent vs population number of people").update_layout(
    xaxis_title="waste percent", yaxis_title="population"
)
st.plotly_chart(fig)
st.write("Using the data shown above, it is clear that the population and the waste percentage do not correlate, since waste percentages vary regardless of population size")
st.markdown("""---""")
         
st.header("The Effect of Waste Management Laws on the Total Amount of MSW Produced in Countries")
st.write("Does a national law governing waste management in a country decrease the total waste produced in that country?")
fig = px.scatter(my_dataset, x="total_msw_total_msw_generated_tons_year", size="total_msw_total_msw_generated_tons_year", color="other_information_national_law_governing_solid_waste_management_in_the_country", hover_name="country_name", log_x=True, size_max=60, color_discrete_sequence=["cornflowerblue", "crimson"], title="Effect of Waste Management Laws on the Total Amount of Municipal Solid Waste (MSW) Produced in Countries")
fig.update_layout(legend_title_text='National Law Governing Solid Waste Management')
st.plotly_chart(fig)
st.write("A national law governing waste management in a country does not decrease the total waste produced in that country. The countries that produced the most amount of municipal solid waste (MSW) had national laws governing solid waste.")

st.markdown("""---""")
###Jeffreys 3rd
st.header("Does GDP and having agencys to enforce solid waste laws correspond")

fig = px.scatter(my_dataset, y="gdp", x='population_population_number_of_people', size = 'population_population_number_of_people', hover_data = ['country_name'], color = 'other_information_national_agency_to_enforce_solid_waste_laws_and_regulations', size_max=50, title = 'Does GDP and having agencys to enforce solid waste laws correspond',color_discrete_sequence=['cornflowerblue', "crimson"])

fig.update_layout(legend_title_text='National Law Governing Solid Waste Management')
st.plotly_chart(fig)
st.write('No. A national law that enforces solid waste regulations does not affect the GDP( gross domestic product).')


#Always good to section out your code for readability.
st.header('Conclusions')
st.write('To summarize our groups thoughts, we created data analyzing how different countries pollution laws and rates may differ. As we analyzed the different amounts of waste produced by countries, we found that 1) The EAS produces the most plastic, while the ECS produces the least, and 2) Glass waste appears to be more common than metal waste. In addition to these discoveries, laws governing waste do not affect a countrys waste amount. Our graphs provide further insight into these statistics, and you might be surprised at what we found!')

