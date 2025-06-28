# F1 Capstone
## 

This is a continuation of my exploration of the world of freely available F1 data!
This time around, the goal is to create a machine learning model to try to predict a driver's race finishing position at a given race.

The final product will be an interactable Streamlit app that allows the user to filter by race and drive to see model predictions.
The app with the 2024 season can be found [...coming soon!](app link)
2025 Season to also be added soon.

## Data Sources

Two publicly-available APIs:

- ~~Ergast~~ - no longer active, but all available data was pulled
- [OpenF1](https://openf1.org/)

## Methodology

Using Python / Pandas, data was cleaned and useful model features were added. All available years were included (1950 - 2024) for feature engineering, and then the dataset was filtered down to 2001 - onward for model building. Data was further split into 2001-2023 for model training, with 2024 set aside as test data.

(note about why only 2021 onwards was used):

The models used were the Scikit Learn Logistic Regression model (as a baseline, because of its explainability), and the LightGBM Classifier for its better performance (relative to the LogReg).

## Limitations

The model is based on historical *driver* performance, however the car is (anecdotally) actually reponsible for 90% of performance, so changes to sporting regulations (i.e. how cars are allowed to be constructed) from year to year may affect results in ways the model can't anticipate (and may be slow to react to).
Pre-race session performance (free practice and qualifying sessions) may be a good indicator of performance in the race, but only have that data for 2023-2025, so difficult to incorporate at the moment.

## Future Exploration
- More feature engineering (can one ever have enough?)
- Trying other high-performing models.
- More data - what other accessible repositories are out there?
