import pandas as pd  # Import the pandas library for data manipulation
import numpy as np  # Import the numpy library for numerical operations
import instaloader  # Import the instaloader library for interacting with Instagram

# Function to log in to Instagram


def login_instagram():
    # Prompt the user for their username
    user = input("Enter your Instagram username: ")
    # Prompt the user for their password
    password = input("Enter your Instagram password: ")
    loader = instaloader.Instaloader()  # Create an Instaloader object
    # Log in to Instagram using the provided credentials
    loader.login(user, password)
    return loader  # Return the Instaloader object

# Function to retrieve profile data (followers and followees)


def get_profile_data(loader):
    # Prompt the user for the target profile username
    target_profile = input(
        "Enter the username of the profile to compare followers and followees: ")
    profile = instaloader.Profile.from_username(
        loader.context, target_profile)  # Get the target profile object
    # Get the followers of the target profile as a pandas Series
    df_followers = pd.Series(profile.get_followers())
    # Get the followees of the target profile as a pandas Series
    df_followees = pd.Series(profile.get_followees())
    # Return a DataFrame containing followers and followees
    return pd.DataFrame({'followers': df_followers, 'followees': df_followees})

# Function to clean the data


def clean_data(inst_sub):
    inst_sub['followers'] = inst_sub['followers'].astype(
        str)  # Convert the 'followers' column to string type
    inst_sub['followees'] = inst_sub['followees'].astype(
        str)  # Convert the 'followees' column to string type
    # Fill missing values in the 'followees' column with "0"
    inst_sub = inst_sub.fillna({'followees': "0"})

    # Get the column index of 'followers'
    loc_0 = inst_sub.columns.get_loc('followers')
    inst_sub_split = inst_sub['followers'].str.split(expand=True).add_prefix(
        'followers_')  # Split the 'followers' column and add a prefix to the new columns
    # Concatenate the split columns with the original DataFrame
    inst_sub = pd.concat(
        [inst_sub.iloc[:, :loc_0], inst_sub_split, inst_sub.iloc[:, loc_0:]], axis=1)

    # Get the column index of 'followees'
    loc_1 = inst_sub.columns.get_loc('followees')
    inst_sub_split = inst_sub['followees'].str.split(expand=True).add_prefix(
        'followees_')  # Split the 'followees' column and add a prefix to the new columns
    # Concatenate the split columns with the original DataFrame
    inst_sub = pd.concat(
        [inst_sub.iloc[:, :loc_1], inst_sub_split, inst_sub.iloc[:, loc_1:]], axis=1)

    inst_sub = inst_sub.drop(columns=['followers', 'followees', 'followers_0',
                             'followers_2', 'followees_0', 'followees_2'])  # Drop unnecessary columns
    # Rename the relevant columns
    inst_sub = inst_sub.rename(
        columns={'followers_1': 'followers', 'followees_1': 'followees'})
    return inst_sub  # Return the cleaned DataFrame

# Main function


def main():
    loader = login_instagram()  # Log in to Instagram
    inst_sub = get_profile_data(loader)  # Get profile data

    inst_sub_clean = clean_data(inst_sub.copy())  # Clean the data

    inst_sub_clean['followers'] = inst_sub_clean['followers'].astype(
        str)  # Convert 'followers' to string
    inst_sub_clean['followees'] = inst_sub_clean['followees'].astype(
        str)  # Convert 'followees' to string
    # Fill missing values in 'followees'
    inst_sub_clean = inst_sub_clean.fillna({'followees': "0"})

    # Find the difference between followees and followers
    inst_sub_clean = pd.Series(np.setdiff1d(
        inst_sub_clean['followees'], inst_sub_clean['followers']))
    # Save the cleaned data to a CSV file
    inst_sub_clean.to_csv('clean_data.csv', index=False, header=False)

    # Print a message indicating successful data cleaning
    print("Data has been cleaned and saved to 'clean_data.csv'")


# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
