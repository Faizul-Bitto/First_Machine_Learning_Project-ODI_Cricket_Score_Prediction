# Import necessary modules for the Flask web application
from flask import Flask, render_template, request
import pickle
import pandas as pd

# A Flask web application instance
app = Flask(__name__)

# Load the trained model and other data
pipe = pickle.load(open('XGB_pipeline.pkl', 'rb'))

teams = ['Afghanistan',
         'Australia',
         'Bangladesh',
         'England',
         'India',
         'Ireland',
         'Kenya',
         'Netherlands',
         'New Zealand',
         'Pakistan',
         'Scotland',
         'South Africa',
         'Sri Lanka',
         'West Indies',
         'Zimbabwe']

cities = ['Aberdeen', 'Abu Dhabi', 'Adelaide', 'Ahmedabad', 'Amstelveen', 'Antigua', 'Auckland', 'Ayr', 'Bangalore', 'Barbados', 'Belfast', 'Bengaluru', 'Benoni', 'Birmingham', 'Bloemfontein', 'Bogra', 'Bready', 'Bridgetown', 'Brisbane', 'Bristol', 'Bulawayo', 'Cairns', 'Canberra', 'Canterbury', 'Cape Town', 'Cardiff', 'Centurion', 'Chandigarh', 'Chattogram', 'Chelmsford', 'Chennai', 'Chester-le-Street', 'Chittagong', 'Christchurch', 'Colombo', 'Cuttack', 'Dambulla', 'Darwin', 'Dehra Dun', 'Delhi', 'Deventer', 'Dhaka', 'Dharamsala', 'Dharmasala', 'Doha', 'Dominica', 'Dubai', 'Dublin', 'Dunedin', 'Durban', 'East London', 'Edinburgh', 'Faisalabad', 'Faridabad', 'Fatullah', 'Galle', 'Glasgow', 'Gqeberha', 'Greater Noida', 'Grenada', 'Gros Islet', 'Guwahati', 'Guyana', 'Gwalior', 'Hambantota', 'Hamilton', 'Harare', 'Hobart', 'Hyderabad',
          'Indore', 'Jaipur', 'Jamaica', 'Jamshedpur', 'Johannesburg', 'Kandy', 'Kanpur', 'Karachi', 'Khulna', 'Kimberley', 'Kingston', 'Kingstown', 'Kochi', 'Kolkata', 'Kuala Lumpur', 'Lahore', 'Leeds', 'Lincoln', 'London', 'Lucknow', 'Manchester', 'Margao', 'Melbourne', 'Mirpur', 'Mombasa', 'Mount Maunganui', 'Multan', 'Mumbai', 'Nagpur', 'Nairobi', 'Napier', 'Nelson', 'North Sound', 'Nottingham', 'Paarl', 'Pallekele', 'Perth', 'Peshawar', 'Port Elizabeth', 'Port of Spain', 'Potchefstroom', 'Providence', 'Pune', 'Queenstown', 'Raipur', 'Rajkot', 'Ranchi', 'Rangiri', 'Rawalpindi', 'Rotterdam', 'Sharjah', 'Sheikhupura', 'Sind', 'Southampton', "St George's", 'St Kitts', 'St Lucia', 'St Vincent', 'Sydney', 'Sylhet', 'Tarouba', 'Taunton', 'Thiruvananthapuram', 'Townsville', 'Trinidad', 'Utrecht', 'Vadodara', 'Visakhapatnam', 'Wellington', 'Whangarei']

toss_decision_from_winner = ['bat', 'field']

venue = ['AMI Stadium', 'Adelaide Oval', 'Andhra Cricket Association-Visakhapatnam District Cricket Association Stadium', "Antigua Recreation Ground, St John's", 'Arbab Niaz Stadium', 'Arnos Vale Ground', 'Arnos Vale Ground, Kingstown', 'Arnos Vale Ground, Kingstown, St Vincent', 'Arun Jaitley Stadium', 'Arun Jaitley Stadium, Delhi', 'Bangabandhu National Stadium', 'Bangabandhu National Stadium, Dhaka', 'Barabati Stadium', 'Barabati Stadium, Cuttack', 'Barsapara Cricket Stadium', 'Barsapara Cricket Stadium, Guwahati', 'Basin Reserve', 'Bay Oval', 'Bay Oval, Mount Maunganui', 'Beausejour Stadium, Gros Islet', 'Bellerive Oval', 'Bellerive Oval, Hobart', 'Bert Sutcliffe Oval', 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium', 'Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow', 'Boland Bank Park, Paarl', 'Boland Park', 'Boland Park, Paarl', 'Brabourne Stadium', 'Bready Cricket Club, Magheramason', 'Brian Lara Stadium, Tarouba, Trinidad', 'Brisbane Cricket Ground', 'Brisbane Cricket Ground, Woolloongabba', 'Brisbane Cricket Ground, Woolloongabba, Brisbane', 'Buffalo Park', 'Buffalo Park, East London', 'Bulawayo Athletic Club', 'Bundaberg Rum Stadium, Cairns', 'Cambusdoon New Ground', 'Captain Roop Singh Stadium', 'Captain Roop Singh Stadium, Gwalior', 'Carisbrook', 'Castle Avenue', "Cazaly's Stadium, Cairns", 'Chevrolet Park', 'Chittagong Divisional Stadium', 'Civil Service Cricket Club, Stormont', 'Civil Service Cricket Club, Stormont, Belfast', 'Clontarf Cricket Club Ground', 'Clontarf Cricket Club Ground, Dublin', 'Cobham Oval (New)', 'County Ground', 'County Ground, Bristol', 'County Ground, Chelmsford', 'Daren Sammy National Cricket Stadium', 'Daren Sammy National Cricket Stadium, Gros Islet', 'Darren Sammy National Cricket Stadium, Gros Islet', 'Darren Sammy National Cricket Stadium, St Lucia', 'Davies Park, Queenstown', 'De Beers Diamond Oval', 'De Beers Diamond Oval, Kimberley', 'Diamond Oval', 'Diamond Oval, Kimberley', 'Docklands Stadium', 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium', 'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam', 'Dubai International Cricket Stadium', 'Dubai Sports City Cricket Stadium', 'Eden Gardens', 'Eden Gardens, Kolkata', 'Eden Park', 'Eden Park, Auckland', 'Edgbaston', 'Edgbaston, Birmingham', 'Feroz Shah Kotla', 'Gaddafi Stadium', 'Gaddafi Stadium, Lahore', 'Galle International Stadium', 'Goodyear Park', 'Goodyear Park, Bloemfontein', 'Grange Cricket Club Ground, Raeburn Place', 'Grange Cricket Club Ground, Raeburn Place, Edinburgh', 'Grange Cricket Club, Raeburn Place', 'Greater Noida Sports Complex Ground', 'Green Park', 'Greenfield International Stadium', 'Greenfield International Stadium, Thiruvananthapuram', 'Gymkhana Club Ground', 'Gymkhana Club Ground, Nairobi', 'Hagley Oval', 'Hagley Oval, Christchurch', 'Harare Sports Club', 'Hazelaarweg, Rotterdam', 'Headingley', 'Headingley, Leeds', 'Himachal Pradesh Cricket Association Stadium', 'Himachal Pradesh Cricket Association Stadium, Dharamsala', 'Holkar Cricket Stadium', 'Holkar Cricket Stadium, Indore', 'ICC Academy', 'Indian Petrochemicals Corporation Limited Sports Complex Ground', 'Iqbal Stadium', 'Iqbal Stadium, Faisalabad', 'JSCA International Stadium Complex', 'JSCA International Stadium Complex, Ranchi', 'Jade Stadium', 'Jade Stadium, Christchurch', 'John Davies Oval', 'Keenan Stadium', 'Kennington Oval', 'Kennington Oval, London', 'Kensington Oval, Barbados', 'Kensington Oval, Bridgetown', 'Kensington Oval, Bridgetown, Barbados', 'Khan Shaheb Osman Ali Stadium', 'Kingsmead', 'Kingsmead, Durban', 'Kinrara Academy Oval', 'Lal Bahadur Shastri Stadium, Hyderabad, Deccan', "Lord's", "Lord's, London", 'M Chinnaswamy Stadium', 'M Chinnaswamy Stadium, Bengaluru', 'M.Chinnaswamy Stadium', 'MA Aziz Stadium', 'MA Aziz Stadium, Chittagong', 'MA Chidambaram Stadium, Chepauk', 'MA Chidambaram Stadium, Chepauk, Chennai', 'Madhavrao Scindia Cricket Ground', 'Maharani Usharaje Trust Cricket Ground', 'Maharashtra Cricket Association Stadium', 'Maharashtra Cricket Association Stadium, Pune', 'Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa', 'Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa, Hambantota',
         'Malahide', 'Mangaung Oval', 'Mangaung Oval, Bloemfontein', 'Mannofield Park', 'Manuka Oval', 'Marrara Cricket Ground', 'Marrara Cricket Ground, Darwin', 'McLean Park', 'McLean Park, Napier', 'Melbourne Cricket Ground', 'Mombasa Sports Club Ground', 'Multan Cricket Stadium', 'Nahar Singh Stadium', 'Nahar Singh Stadium, Faridabad', 'Narayanganj Osmani Stadium', 'Narendra Modi Stadium, Ahmedabad', 'National Cricket Stadium', 'National Cricket Stadium, Grenada', "National Cricket Stadium, St George's", 'National Stadium', 'National Stadium, Karachi', 'Nehru Stadium', 'Nehru Stadium, Fatorda', 'Nehru Stadium, Poona', 'New Wanderers Stadium', 'New Wanderers Stadium, Johannesburg', 'Newlands', 'Newlands, Cape Town', 'Niaz Stadium, Hyderabad', 'North West Cricket Stadium, Potchefstroom', 'OUTsurance Oval', 'Old Trafford', 'Old Trafford, Manchester', 'P Saravanamuttu Stadium', 'Pallekele International Cricket Stadium', 'Perth Stadium', 'Providence Stadium', 'Providence Stadium, Guyana', 'Punjab Cricket Association IS Bindra Stadium, Mohali', 'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh', 'Punjab Cricket Association Stadium, Mohali', "Queen's Park (New), St George's, Grenada", "Queen's Park Oval", "Queen's Park Oval, Port of Spain", "Queen's Park Oval, Port of Spain, Trinidad", "Queen's Park Oval, Trinidad", 'Queens Sports Club', 'Queens Sports Club, Bulawayo', 'Queenstown Events Centre', 'R Premadasa Stadium', 'R Premadasa Stadium, Colombo', 'R.Premadasa Stadium', 'R.Premadasa Stadium, Khettarama', 'Rajiv Gandhi International Cricket Stadium, Dehradun', 'Rajiv Gandhi International Stadium, Uppal', 'Rajiv Gandhi International Stadium, Uppal, Hyderabad', 'Rangiri Dambulla International Stadium', 'Rawalpindi Cricket Stadium', 'Reliance Stadium', 'Riverside Ground', 'Riverside Ground, Chester-le-Street', 'Riverway Stadium, Townsville', 'Sabina Park, Kingston', 'Sabina Park, Kingston, Jamaica', 'Sardar Patel (Gujarat) Stadium, Motera', 'Sardar Patel Stadium, Motera', 'Saurashtra Cricket Association Stadium', 'Saurashtra Cricket Association Stadium, Rajkot', 'Sawai Mansingh Stadium', 'Saxton Oval', 'Sector 16 Stadium', 'Seddon Park', 'Seddon Park, Hamilton', 'Sedgars Park', 'Sedgars Park, Potchefstroom', 'Senwes Park', 'Senwes Park, Potchefstroom', 'Shaheed Chandu Stadium', 'Shaheed Veer Narayan Singh International Stadium, Raipur', 'Sharjah Cricket Association Stadium', 'Sharjah Cricket Stadium', 'Sheikh Abu Naser Stadium', 'Sheikh Zayed Stadium', 'Sheikhupura Stadium', 'Sher-e-Bangla National Cricket Stadium', 'Shere Bangla National Stadium', 'Shere Bangla National Stadium, Mirpur', 'Sinhalese Sports Club', 'Sinhalese Sports Club Ground', 'Sir Vivian Richards Stadium', 'Sir Vivian Richards Stadium, North Sound', 'Sophia Gardens', 'Sophia Gardens, Cardiff', 'Sportpark Het Schootsveld', 'Sportpark Maarschalkerweerd, Utrecht', "St George's Park", "St George's Park, Port Elizabeth", 'St Lawrence Ground', 'St Lawrence Ground, Canterbury', 'SuperSport Park', 'SuperSport Park, Centurion', 'Sydney Cricket Ground', 'Sylhet International Cricket Stadium', 'Takashinga Sports Club, Highfield, Harare', 'The Cooper Associates County Ground', 'The Rose Bowl', 'The Rose Bowl, Southampton', 'The Royal & Sun Alliance County Ground, Bristol', 'The Village, Malahide', 'The Village, Malahide, Dublin', 'The Wanderers Stadium', 'The Wanderers Stadium, Johannesburg', 'Titwood', 'Tony Ireland Stadium, Townsville', 'Trent Bridge', 'Trent Bridge, Nottingham', 'University Oval', 'VRA Cricket Ground', 'VRA Ground', 'VRA Ground, Amstelveen', 'Vidarbha C.A. Ground', 'Vidarbha Cricket Association Ground', 'Vidarbha Cricket Association Stadium, Jamtha', 'W.A.C.A. Ground', 'Wankhede Stadium', 'Wankhede Stadium, Mumbai', 'Warner Park, Basseterre', 'West End Park International Cricket Stadium, Doha', 'Western Australia Cricket Association Ground', 'Westpac Park, Hamilton', 'Westpac Stadium', 'Westpac Stadium, Wellington', 'Willowmoore Park', 'Willowmoore Park, Benoni', 'Windsor Park, Roseau', 'Zahur Ahmed Chowdhury Stadium', 'Zahur Ahmed Chowdhury Stadium, Chattogram', 'Zohur Ahmed Chowdhury Stadium']


@app.route('/')
def frontpage():
    # Renders the frontpage.html template
    return render_template('frontpage.html')


# Handles both GET and POST requests for the index page
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass

    # Renders the index.html template with provided data
    return render_template('index.html', teams=teams, cities=cities, toss_decisions=toss_decision_from_winner, venues=venue)


@app.route('/predict', methods=['POST'])
def predict():
    # Handles POST requests for the predict page
    if request.method == 'POST':
        # Retrieves form data from the request
        batting_team = request.form['batting_team']
        bowling_team = request.form['bowling_team']
        toss_winner = request.form['toss_winner']
        toss_decision = request.form['toss_decision']
        venue = request.form['venue']
        city = request.form['city']
        current_score = float(request.form['current_score'])
        overs = float(request.form['overs'])
        wickets = float(request.form['wickets'])
        last_five = float(request.form['last_five'])

        # Calculates additional parameters based on form data
        balls_left = 300 - (overs * 6)
        wickets_left = 10 - wickets
        crr = current_score / overs

        # Creates a DataFrame with the form data
        input_df = pd.DataFrame({
            'batting_team': [batting_team],
            'bowling_team': [bowling_team],
            'toss_winner': [toss_winner],
            'toss_decision_from_winner': [toss_decision],
            'city': [city],
            'venue': [venue],
            'current_score': [current_score],
            'balls_left': [balls_left],
            'wickets_left': [wickets],
            'current_run_rate': [crr],
            'last_five': [last_five]
        })

        # Uses a pre-trained model (pipe) to predict the score
        result = pipe.predict(input_df)

        # Renders the result.html template with the predicted score
        return render_template('result.html', predicted_score=int(result[0]))


if __name__ == '__main__':
    # Runs the Flask app in debug mode
    app.run(debug=True)
