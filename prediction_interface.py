import sys
import os
import pandas as pd
import json
import joblib
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QPushButton, QWidget, QComboBox, QMessageBox
)
# Features
# keep features as a placeholder
features = ['Referee_A Madley', 'Referee_A Marriner', 'Referee_A Moss', 'Referee_A Taylor', 'Referee_A Wiley', 'Referee_A. Damato', 'Referee_A. Dattilo', 'Referee_A. De Marco', 'Referee_A. G. Wiley', 'Referee_A. G. Wiley ', 'Referee_A. Giannoccaro', "Referee_A. P. D'Urso", "Referee_A. P. D'Urso ", 'Referee_A. Romeo', 'Referee_A.G. Wiley', 'Referee_Alan Wiley', 'Referee_Albrecht, H', 'Referee_Alfons Berg', 'Referee_Alfons Berg ', "Referee_Andy D'Urso", "Referee_Andy D'Urso ", 'Referee_Andy Hall', 'Referee_Aust, J', 'Referee_B Knight', 'Referee_B. Knight', 'Referee_B. Knight ', 'Referee_B.Zerr ', 'Referee_Barber, G. P.', 'Referee_Barry Knight', 'Referee_Barry, N. S.', 'Referee_Bennett, S. G.', 'Referee_Berg, A', 'Referee_Bernd Heynemann ', 'Referee_C Foy', 'Referee_C Kavanagh', 'Referee_C Pawson', 'Referee_C Wilkes', 'Referee_C. Brighi', 'Referee_C. J. Foy', 'Referee_C. R. Wilkes', 'Referee_C. R. Wilkes ', 'Referee_Clive Wilkes', 'Referee_D Bond', 'Referee_D Coote', 'Referee_D Elleray', 'Referee_D England', 'Referee_D Gallagh', 'Referee_D Gallaghe', 'Referee_D Gallagher', 'Referee_D Pugh', "Referee_D'Urso, A. P.", 'Referee_D. Celi', 'Referee_D. J. Gallagher', 'Referee_D. Messina', 'Referee_D. Orsato', 'Referee_D. Preschern', 'Referee_D. Pugh', 'Referee_D. R. Elleray', 'Referee_D. R. Elleray ', 'Referee_D. Salati', 'Referee_D. Tombolini', 'Referee_David Ellaray', 'Referee_Dean, M. L', 'Referee_Dermot Gallagher', 'Referee_Dowd, P.', 'Referee_Dr. Fleischer, H', 'Referee_Dr. Merk, M', 'Referee_Dunn, S. W.', 'Referee_Durkin, P.', 'Referee_Durkin, P. A.', 'Referee_E Wolstenholme', 'Referee_E. K. Wolstenholme', 'Referee_E. K. Wolstenholme ', 'Referee_E. Morganti', 'Referee_Edgar Steinborn', 'Referee_Edgar Steinborn ', 'Referee_Elleray, D. R.', 'Referee_F Taylor', 'Referee_F. Squillace', 'Referee_Fandel, H', 'Referee_Fleischer, H', 'Referee_Florian Meyer', 'Referee_Florian Meyer ', 'Referee_Foy, C. J.', 'Referee_Franz-Xaver Wack', 'Referee_Franz-Xaver Wack ', 'Referee_Fröhlich, L.-M.', 'Referee_G Barber', 'Referee_G Poll', 'Referee_G Scott', 'Referee_G. Gava', 'Referee_G. Lops', 'Referee_G. P. Barber', 'Referee_G. P. Barber ', 'Referee_G. Paparesta', 'Referee_G. Poll', 'Referee_G. Poll ', 'Referee_G. Rocchi', 'Referee_Gagelmann, P', 'Referee_Gallagher, D. J.', 'Referee_Graham Barber', 'Referee_Graham Poll', 'Referee_H Webb', 'Referee_Halsey, M. R.', 'Referee_Hartmut Strampe', 'Referee_Hartmut Strampe ', 'Referee_Hellmut Krug', 'Referee_Hellmut Krug ', 'Referee_Helmut Fleischer', 'Referee_Helmut Fleischer ', 'Referee_Helmut Krug ', 'Referee_Herbert Fandel', 'Referee_Herbert Fandel ', 'Referee_Herbert Fandell ', 'Referee_Hermann Albrecht', 'Referee_Hermann Albrecht ', 'Referee_I Williamson', 'Referee_Ian Harris', 'Referee_J Brooks', 'Referee_J Gillett', 'Referee_J Gillett ', 'Referee_J Moss', 'Referee_J Smith', 'Referee_J Winter', 'Referee_J. T. Winter', 'Referee_J. T. Winter ', 'Referee_J.T. Winter', 'Referee_Jansen, J', 'Referee_Jeff Winter', 'Referee_Jones, P.', 'Referee_Jörg Kessler', 'Referee_Jörg Kessler ', 'Referee_Jürgen Aust', 'Referee_Jürgen Aust ', 'Referee_Jürgen Jansen', 'Referee_Jürgen Jansen ', 'Referee_K Friend', 'Referee_K Stroud', 'Referee_Kemmling, U', 'Referee_Kessler, J', 'Referee_Keßler, J', 'Referee_Kinhöfer, T', 'Referee_Kircher, K', 'Referee_Knight, B.', 'Referee_Knut Kircher', 'Referee_Koop, T', 'Referee_Krug, H', 'Referee_Krug, H.', 'Referee_L Mason', 'Referee_L Probert', 'Referee_L Smith', 'Referee_L. Banti', 'Referee_L. Marelli', 'Referee_L. Palanca', 'Referee_Lutz Michael Fröhlich', 'Referee_Lutz Michael Fröhlich ', 'Referee_Lutz Wagner', 'Referee_Lutz Wagner ', 'Referee_Lutz-Michael Froehlich', 'Referee_Lutz-Michael Fröhlich', 'Referee_M Atkinson', 'Referee_M Clattenburg', 'Referee_M Dean', 'Referee_M Donohue', 'Referee_M Halsey', 'Referee_M Jones', 'Referee_M Messias', 'Referee_M Oliver', 'Referee_M Riley', 'Referee_M Salisbury', 'Referee_M. A. Riley', 'Referee_M. A. Riley ', 'Referee_M. Bergonzi', 'Referee_M. Ciampi', 'Referee_M. D. Messias', 'Referee_M. De Santis', 'Referee_M. Gabriele', 'Referee_M. Girard', 'Referee_M. L Dean', 'Referee_M. L. Dean', 'Referee_M. Mazzoleni', 'Referee_M. R. Halsey', 'Referee_M. Saccani', 'Referee_M. Trefoloni', 'Referee_M. Velotto', 'Referee_Mark Halsey', 'Referee_Mark Halsey ', 'Referee_Markus Merk', 'Referee_Markus Merk ', 'Referee_Matt Messias', 'Referee_Merk, M', 'Referee_Messias, M. D.', 'Referee_Meyer, F', 'Referee_Michael Weiner', 'Referee_Michael Weiner ', 'Referee_Mike Dean', 'Referee_Mike Riley', 'Referee_Mn Atkinson', 'Referee_N Barry', 'Referee_N Swarbrick', 'Referee_N. Ayroldi', 'Referee_N. Pierpaoli', 'Referee_N. Rizzoli', 'Referee_N. S. Barry', 'Referee_N. Stefanini', 'Referee_Neale Barry', 'Referee_O Langford', 'Referee_O. Girardi', 'Referee_O. Pantana', 'Referee_P Bankes', 'Referee_P Crossley', 'Referee_P Dowd', 'Referee_P Durkin', 'Referee_P Tierney', 'Referee_P Walton', 'Referee_P. A. Durkin', 'Referee_P. A. Durkin ', 'Referee_P. Bertini', 'Referee_P. Dondarini', 'Referee_P. Dowd', 'Referee_P. Jones', 'Referee_P. Jones ', 'Referee_P. Mazzoleni', 'Referee_P. Rodomonti', 'Referee_P. Tagliavento', 'Referee_P.A. Durkin', 'Referee_Paul Durkin', 'Referee_Paul Taylor', 'Referee_Peter Gagelmann', 'Referee_Peter Gagelmann ', 'Referee_Peter Jones', 'Referee_Peter Sippel', 'Referee_Peter Sippel ', 'Referee_Poll, G.', 'Referee_Pugh, D.', 'Referee_R Beeby', 'Referee_R East', 'Referee_R Jones', 'Referee_R Madley', 'Referee_R Martin', 'Referee_R Styles', 'Referee_R Welch', 'Referee_R. Herberg', 'Referee_R. Rosetti', 'Referee_R. Styles', 'Referee_Rennie, U. D.', 'Referee_Riley, M. A.', 'Referee_Rob Harris', 'Referee_Rob Styles', 'Referee_Roy Burton', 'Referee_S Allison', 'Referee_S Attwell', 'Referee_S Barrott', 'Referee_S Bennett', 'Referee_S Dunn', 'Referee_S Hooper', 'Referee_S Scott', 'Referee_S Singh', 'Referee_S Tanner', "Referee_S. Cassara'", 'Referee_S. Farina', 'Referee_S. G. Bennett', 'Referee_S. Racalbuto', 'Referee_S. W. Dunn', 'Referee_S. W. Dunn ', 'Referee_Sippel, P', 'Referee_St Bennett', 'Referee_Stark, W', 'Referee_Steinborn, E.', 'Referee_Steve Bennett', 'Referee_Steve Bennett ', 'Referee_Steve Dunn', 'Referee_Steve Lodge', 'Referee_Strampe, H', 'Referee_Styles, R', 'Referee_Styles, R.', 'Referee_T Bramall', 'Referee_T Harrington', 'Referee_T Robinson', 'Referee_T. Pieri', 'Referee_Thorsten Kinhöfer ', 'Referee_Torsten Koop', 'Referee_Torsten Koop ', 'Referee_U Rennie', 'Referee_U. D. Rennie', 'Referee_Uwe Kemmling', 'Referee_Uwe Kemmling ', 'Referee_Wack, F.-X.', 'Referee_Wagner, L', 'Referee_Weiner, M', 'Referee_Wiley, A. G.', 'Referee_Wilkes, C. R.', 'Referee_Winter, J. T.', 'Referee_Wolfgang Stark', 'Referee_Wolfgang Stark ', 'Referee_Wolstenholme, E. K.', 'Referee_Yates, N', 'Referee_l Mason', "Referee_\xa0A D'Urso", 'Referee_\xa0A Wiley', 'Referee_\xa0C Foy', 'Referee_\xa0D Gallagher', 'Referee_\xa0H Webb', 'Referee_\xa0M Atkinson', 'Referee_\xa0N Barry', 'Referee_\xa0S Dunn', 'Referee_\xa0U Rennie', 'HomeTeam_Ajaccio', 'HomeTeam_Ajaccio GFCO', 'HomeTeam_Alaves', 'HomeTeam_Albacete', 'HomeTeam_Almeria', 'HomeTeam_Amiens', 'HomeTeam_Ancona', 'HomeTeam_Angers', 'HomeTeam_Arles', 'HomeTeam_Arsenal', 'HomeTeam_Ascoli', 'HomeTeam_Aston Villa', 'HomeTeam_Atalanta', 'HomeTeam_Ath Bilbao', 'HomeTeam_Ath Madrid', 'HomeTeam_Augsburg', 'HomeTeam_Auxerre', 'HomeTeam_Barcelona', 'HomeTeam_Bari', 'HomeTeam_Barnsley', 'HomeTeam_Bastia', 'HomeTeam_Bayern Munich', 'HomeTeam_Benevento', 'HomeTeam_Betis', 'HomeTeam_Bielefeld', 'HomeTeam_Birmingham', 'HomeTeam_Blackburn', 'HomeTeam_Blackpool', 'HomeTeam_Bochum', 'HomeTeam_Bologna', 'HomeTeam_Bolton', 'HomeTeam_Bordeaux', 'HomeTeam_Boulogne', 'HomeTeam_Bournemouth', 'HomeTeam_Bradford', 'HomeTeam_Braunschweig', 'HomeTeam_Brentford', 'HomeTeam_Brescia', 'HomeTeam_Brest', 'HomeTeam_Brighton', 'HomeTeam_Burnley', 'HomeTeam_Cadiz', 'HomeTeam_Caen', 'HomeTeam_Cagliari', 'HomeTeam_Cannes', 'HomeTeam_Cardiff', 'HomeTeam_Carpi', 'HomeTeam_Catania', 'HomeTeam_Celta', 'HomeTeam_Cesena', 'HomeTeam_Charlton', 'HomeTeam_Chateauroux', 'HomeTeam_Chelsea', 'HomeTeam_Chievo', 'HomeTeam_Clermont', 'HomeTeam_Como', 'HomeTeam_Compostela', 'HomeTeam_Cordoba', 'HomeTeam_Cottbus', 'HomeTeam_Coventry', 'HomeTeam_Cremonese', 'HomeTeam_Crotone', 'HomeTeam_Crystal Palace', 'HomeTeam_Darmstadt', 'HomeTeam_Derby', 'HomeTeam_Dijon', 'HomeTeam_Dortmund', 'HomeTeam_Dresden', 'HomeTeam_Duisburg', 'HomeTeam_Dusseldorf', 'HomeTeam_Eibar', 'HomeTeam_Ein Frankfurt', 'HomeTeam_Elche', 'HomeTeam_Empoli', 'HomeTeam_Espanol', 'HomeTeam_Everton', 'HomeTeam_Evian Thonon Gaillard', 'HomeTeam_Extremadura', 'HomeTeam_FC Koln', 'HomeTeam_Fiorentina', 'HomeTeam_Foggia', 'HomeTeam_Fortuna Dusseldorf', 'HomeTeam_Freiburg', 'HomeTeam_Frosinone', 'HomeTeam_Fulham', 'HomeTeam_Genoa', 'HomeTeam_Getafe', 'HomeTeam_Gimnastic', 'HomeTeam_Girona', 'HomeTeam_Granada', 'HomeTeam_Grenoble', 'HomeTeam_Greuther Furth', 'HomeTeam_Gueugnon', 'HomeTeam_Guingamp', 'HomeTeam_Hamburg', 'HomeTeam_Hannover', 'HomeTeam_Hansa Rostock', 'HomeTeam_Heidenheim', 'HomeTeam_Hercules', 'HomeTeam_Hertha', 'HomeTeam_Hoffenheim', 'HomeTeam_Holstein Kiel', 'HomeTeam_Huddersfield', 'HomeTeam_Huesca', 'HomeTeam_Hull', 'HomeTeam_Ingolstadt', 'HomeTeam_Inter', 'HomeTeam_Ipswich', 'HomeTeam_Istres', 'HomeTeam_Juventus', 'HomeTeam_Kaiserslautern', 'HomeTeam_Karlsruhe', 'HomeTeam_La Coruna', 'HomeTeam_Las Palmas', 'HomeTeam_Lazio', 'HomeTeam_Le Havre', 'HomeTeam_Le Mans', 'HomeTeam_Lecce', 'HomeTeam_Leeds', 'HomeTeam_Leganes', 'HomeTeam_Leicester', 'HomeTeam_Leipzig', 'HomeTeam_Lens', 'HomeTeam_Lerida', 'HomeTeam_Levante', 'HomeTeam_Leverkusen', 'HomeTeam_Lille', 'HomeTeam_Liverpool', 'HomeTeam_Livorno', 'HomeTeam_Logrones', 'HomeTeam_Lorient', 'HomeTeam_Luton', 'HomeTeam_Lyon', "HomeTeam_M'Gladbach", "HomeTeam_M'gladbach", 'HomeTeam_Mainz', 'HomeTeam_Malaga', 'HomeTeam_Mallorca', 'HomeTeam_Man City', 'HomeTeam_Man United', 'HomeTeam_Marseille', 'HomeTeam_Martigues', 'HomeTeam_Merida', 'HomeTeam_Messina', 'HomeTeam_Metz', 'HomeTeam_Middlesbrough', 'HomeTeam_Milan', 'HomeTeam_Modena', 'HomeTeam_Monaco', 'HomeTeam_Montpellier', 'HomeTeam_Monza', 'HomeTeam_Munich 1860', 'HomeTeam_Murcia', 'HomeTeam_Nancy', 'HomeTeam_Nantes', 'HomeTeam_Napoli', 'HomeTeam_Newcastle', 'HomeTeam_Nice', 'HomeTeam_Nimes', 'HomeTeam_Norwich', "HomeTeam_Nott'm Forest", 'HomeTeam_Novara', 'HomeTeam_Numancia', 'HomeTeam_Nurnberg', 'HomeTeam_Oldham', 'HomeTeam_Osasuna', 'HomeTeam_Oviedo', 'HomeTeam_Paderborn', 'HomeTeam_Padova', 'HomeTeam_Palermo', 'HomeTeam_Paris SG', 'HomeTeam_Parma', 'HomeTeam_Perugia', 'HomeTeam_Pescara', 'HomeTeam_Piacenza', 'HomeTeam_Portsmouth', 'HomeTeam_QPR', 'HomeTeam_RB Leipzig', 'HomeTeam_Reading', 'HomeTeam_Real Madrid', 'HomeTeam_Recreativo', 'HomeTeam_Reggiana', 'HomeTeam_Reggina', 'HomeTeam_Reims', 'HomeTeam_Rennes', 'HomeTeam_Roma', 'HomeTeam_Salamanca', 'HomeTeam_Salernitana', 'HomeTeam_Sampdoria', 'HomeTeam_Santander', 'HomeTeam_Sassuolo', 'HomeTeam_Schalke 04', 'HomeTeam_Sedan', 'HomeTeam_Sevilla', 'HomeTeam_Sheffield United', 'HomeTeam_Sheffield Weds', 'HomeTeam_Siena', 'HomeTeam_Sochaux', 'HomeTeam_Sociedad', 'HomeTeam_Southampton', 'HomeTeam_Sp Gijon', 'HomeTeam_Spal', 'HomeTeam_Spezia', 'HomeTeam_St Etienne', 'HomeTeam_St Pauli', 'HomeTeam_Stoke', 'HomeTeam_Strasbourg', 'HomeTeam_Stuttgart', 'HomeTeam_Sunderland', 'HomeTeam_Swansea', 'HomeTeam_Swindon', 'HomeTeam_Tenerife', 'HomeTeam_Torino', 'HomeTeam_Tottenham', 'HomeTeam_Toulouse', 'HomeTeam_Treviso', 'HomeTeam_Troyes', 'HomeTeam_Udinese', 'HomeTeam_Uerdingen', 'HomeTeam_Ulm', 'HomeTeam_Union Berlin', 'HomeTeam_Unterhaching', 'HomeTeam_Valencia', 'HomeTeam_Valenciennes', 'HomeTeam_Valladolid', 'HomeTeam_Vallecano', 'HomeTeam_Venezia', 'HomeTeam_Verona', 'HomeTeam_Vicenza', 'HomeTeam_Villareal', 'HomeTeam_Villarreal', 'HomeTeam_Watford', 'HomeTeam_Wattenscheid', 'HomeTeam_Werder Bremen', 'HomeTeam_West Brom', 'HomeTeam_West Ham', 'HomeTeam_Wigan', 'HomeTeam_Wimbledon', 'HomeTeam_Wolfsburg', 'HomeTeam_Wolves', 'HomeTeam_Xerez', 'HomeTeam_Zaragoza', 'AwayTeam_Ajaccio', 'AwayTeam_Ajaccio GFCO', 'AwayTeam_Alaves', 'AwayTeam_Albacete', 'AwayTeam_Almeria', 'AwayTeam_Amiens', 'AwayTeam_Ancona', 'AwayTeam_Angers', 'AwayTeam_Arles', 'AwayTeam_Arsenal', 'AwayTeam_Ascoli', 'AwayTeam_Aston Villa', 'AwayTeam_Atalanta', 'AwayTeam_Ath Bilbao', 'AwayTeam_Ath Madrid', 'AwayTeam_Augsburg', 'AwayTeam_Auxerre', 'AwayTeam_Barcelona', 'AwayTeam_Bari', 'AwayTeam_Barnsley', 'AwayTeam_Bastia', 'AwayTeam_Bayern Munich', 'AwayTeam_Benevento', 'AwayTeam_Betis', 'AwayTeam_Bielefeld', 'AwayTeam_Birmingham', 'AwayTeam_Blackburn', 'AwayTeam_Blackpool', 'AwayTeam_Bochum', 'AwayTeam_Bologna', 'AwayTeam_Bolton', 'AwayTeam_Bordeaux', 'AwayTeam_Boulogne', 'AwayTeam_Bournemouth', 'AwayTeam_Bradford', 'AwayTeam_Braunschweig', 'AwayTeam_Brentford', 'AwayTeam_Brescia', 'AwayTeam_Brest', 'AwayTeam_Brighton', 'AwayTeam_Burnley', 'AwayTeam_Cadiz', 'AwayTeam_Caen', 'AwayTeam_Cagliari', 'AwayTeam_Cannes', 'AwayTeam_Cardiff', 'AwayTeam_Carpi', 'AwayTeam_Catania', 'AwayTeam_Celta', 'AwayTeam_Cesena', 'AwayTeam_Charlton', 'AwayTeam_Chateauroux', 'AwayTeam_Chelsea', 'AwayTeam_Chievo', 'AwayTeam_Clermont', 'AwayTeam_Como', 'AwayTeam_Compostela', 'AwayTeam_Cordoba', 'AwayTeam_Cottbus', 'AwayTeam_Coventry', 'AwayTeam_Cremonese', 'AwayTeam_Crotone', 'AwayTeam_Crystal Palace', 'AwayTeam_Darmstadt', 'AwayTeam_Derby', 'AwayTeam_Dijon', 'AwayTeam_Dortmund', 'AwayTeam_Dresden', 'AwayTeam_Duisburg', 'AwayTeam_Dusseldorf', 'AwayTeam_Eibar', 'AwayTeam_Ein Frankfurt', 'AwayTeam_Elche', 'AwayTeam_Empoli', 'AwayTeam_Espanol', 'AwayTeam_Everton', 'AwayTeam_Evian Thonon Gaillard', 'AwayTeam_Extremadura', 'AwayTeam_FC Koln', 'AwayTeam_Fiorentina', 'AwayTeam_Foggia', 'AwayTeam_Fortuna Dusseldorf', 'AwayTeam_Freiburg', 'AwayTeam_Frosinone', 'AwayTeam_Fulham', 'AwayTeam_Genoa', 'AwayTeam_Getafe', 'AwayTeam_Gimnastic', 'AwayTeam_Girona', 'AwayTeam_Granada', 'AwayTeam_Grenoble', 'AwayTeam_Greuther Furth', 'AwayTeam_Gueugnon', 'AwayTeam_Guingamp', 'AwayTeam_Hamburg', 'AwayTeam_Hannover', 'AwayTeam_Hansa Rostock', 'AwayTeam_Heidenheim', 'AwayTeam_Hercules', 'AwayTeam_Hertha', 'AwayTeam_Hoffenheim', 'AwayTeam_Holstein Kiel', 'AwayTeam_Huddersfield', 'AwayTeam_Huesca', 'AwayTeam_Hull', 'AwayTeam_Ingolstadt', 'AwayTeam_Inter', 'AwayTeam_Ipswich', 'AwayTeam_Istres', 'AwayTeam_Juventus', 'AwayTeam_Kaiserslautern', 'AwayTeam_Karlsruhe', 'AwayTeam_La Coruna', 'AwayTeam_Las Palmas', 'AwayTeam_Lazio', 'AwayTeam_Le Havre', 'AwayTeam_Le Mans', 'AwayTeam_Lecce', 'AwayTeam_Leeds', 'AwayTeam_Leganes', 'AwayTeam_Leicester', 'AwayTeam_Leipzig', 'AwayTeam_Lens', 'AwayTeam_Lerida', 'AwayTeam_Levante', 'AwayTeam_Leverkusen', 'AwayTeam_Lille', 'AwayTeam_Liverpool', 'AwayTeam_Livorno', 'AwayTeam_Logrones', 'AwayTeam_Lorient', 'AwayTeam_Luton', 'AwayTeam_Lyon', "AwayTeam_M'Gladbach", "AwayTeam_M'gladbach", 'AwayTeam_Mainz', 'AwayTeam_Malaga', 'AwayTeam_Mallorca', 'AwayTeam_Man City', 'AwayTeam_Man United', 'AwayTeam_Marseille', 'AwayTeam_Martigues', 'AwayTeam_Merida', 'AwayTeam_Messina', 'AwayTeam_Metz', 'AwayTeam_Middlesbrough', 'AwayTeam_Milan', 'AwayTeam_Modena', 'AwayTeam_Monaco', 'AwayTeam_Montpellier', 'AwayTeam_Monza', 'AwayTeam_Munich 1860', 'AwayTeam_Murcia', 'AwayTeam_Nancy', 'AwayTeam_Nantes', 'AwayTeam_Napoli', 'AwayTeam_Newcastle', 'AwayTeam_Nice', 'AwayTeam_Nimes', 'AwayTeam_Norwich', "AwayTeam_Nott'm Forest", 'AwayTeam_Novara', 'AwayTeam_Numancia', 'AwayTeam_Nurnberg', 'AwayTeam_Oldham', 'AwayTeam_Osasuna', 'AwayTeam_Oviedo', 'AwayTeam_Paderborn', 'AwayTeam_Padova', 'AwayTeam_Palermo', 'AwayTeam_Paris SG', 'AwayTeam_Parma', 'AwayTeam_Perugia', 'AwayTeam_Pescara', 'AwayTeam_Piacenza', 'AwayTeam_Portsmouth', 'AwayTeam_QPR', 'AwayTeam_RB Leipzig', 'AwayTeam_Reading', 'AwayTeam_Real Madrid', 'AwayTeam_Recreativo', 'AwayTeam_Reggiana', 'AwayTeam_Reggina', 'AwayTeam_Reims', 'AwayTeam_Rennes', 'AwayTeam_Roma', 'AwayTeam_Salamanca', 'AwayTeam_Salernitana', 'AwayTeam_Sampdoria', 'AwayTeam_Santander', 'AwayTeam_Sassuolo', 'AwayTeam_Schalke 04', 'AwayTeam_Sedan', 'AwayTeam_Sevilla', 'AwayTeam_Sheffield United', 'AwayTeam_Sheffield Weds', 'AwayTeam_Siena', 'AwayTeam_Sochaux', 'AwayTeam_Sociedad', 'AwayTeam_Southampton', 'AwayTeam_Sp Gijon', 'AwayTeam_Spal', 'AwayTeam_Spezia', 'AwayTeam_St Etienne', 'AwayTeam_St Pauli', 'AwayTeam_Stoke', 'AwayTeam_Strasbourg', 'AwayTeam_Stuttgart', 'AwayTeam_Sunderland', 'AwayTeam_Swansea', 'AwayTeam_Swindon', 'AwayTeam_Tenerife', 'AwayTeam_Torino', 'AwayTeam_Tottenham', 'AwayTeam_Toulouse', 'AwayTeam_Treviso', 'AwayTeam_Troyes', 'AwayTeam_Udinese', 'AwayTeam_Uerdingen', 'AwayTeam_Ulm', 'AwayTeam_Union Berlin', 'AwayTeam_Unterhaching', 'AwayTeam_Valencia', 'AwayTeam_Valenciennes', 'AwayTeam_Valladolid', 'AwayTeam_Vallecano', 'AwayTeam_Venezia', 'AwayTeam_Verona', 'AwayTeam_Vicenza', 'AwayTeam_Villareal', 'AwayTeam_Villarreal', 'AwayTeam_Watford', 'AwayTeam_Wattenscheid', 'AwayTeam_Werder Bremen', 'AwayTeam_West Brom', 'AwayTeam_West Ham', 'AwayTeam_Wigan', 'AwayTeam_Wimbledon', 'AwayTeam_Wolfsburg', 'AwayTeam_Wolves', 'AwayTeam_Xerez', 'AwayTeam_Zaragoza', 'HomeTeamShots', 'AwayTeamShots', 'HomeTeamShotsOnTarget', 'AwayTeamShotsOnTarget', 'HomeTeamFoulsCommitted', 'AwayTeamFoulsCommitted', 'HomeTeamCorners', 'AwayTeamCorners', 'HomeTeamYellowCards', 'AwayTeamYellowCards', 'HomeTeamRedCards', 'AwayTeamRedCards']

# Load models
models = {}
models["1.5U_model"]        = joblib.load(r"C:\Users\kagan\SpyderScripts\FootballMatchPrediction\Models\1.5U_classifier_model.joblib")
models["2.5U_model"]        = joblib.load(r"C:\Users\kagan\SpyderScripts\FootballMatchPrediction\Models\2.5U_classifier_model.joblib")
models["AwayTeamWin_model"] = joblib.load(r"C:\Users\kagan\SpyderScripts\FootballMatchPrediction\Models\AwayTeamWin_classifier_model.joblib")
models["Draw_model"]        = joblib.load(r"C:\Users\kagan\SpyderScripts\FootballMatchPrediction\Models\Draw_classifier_model.joblib")
models["HomeTeamWin_model"] = joblib.load(r"C:\Users\kagan\SpyderScripts\FootballMatchPrediction\Models\HomeTeamWin_classifier_model.joblib")


# Input formatting function
def format_input(referee, 
                 home_team, 
                 away_team, 
                 home_team_shots,
                 away_team_shots,
                 home_team_shots_on_target,
                 away_team_shots_on_target,
                 home_team_fouls_committed,
                 away_team_fouls_committed,
                 home_team_corners,
                 away_team_corners,
                 home_team_yellow_cards,
                 away_team_yellow_cards,
                 home_team_red_cards,
                 away_team_red_cards):
    """
    Formats input data for prediction, ensuring alignment with the model's expected predictors.
    """
    # Initialize an input dictionary with all zeros for the expected predictors
    input_data = {col: 0 for col in features}
    
    # Map inputs
    input_data[f"Referee_{referee}"] = 1
    input_data[f"HomeTeam_{home_team}"] = 1
    input_data[f"AwayTeam_{away_team}"] = 1
    input_data["HomeTeamShots"] = home_team_shots
    input_data["AwayTeamShots"] = away_team_shots
    input_data["HomeTeamShotsOnTarget"] = home_team_shots_on_target
    input_data["AwayTeamShotsOnTarget"] = away_team_shots_on_target
    input_data["HomeTeamFoulsCommitted"] = home_team_fouls_committed
    input_data["AwayTeamFoulsCommitted"] = away_team_fouls_committed
    input_data["HomeTeamCorners"] = home_team_corners
    input_data["AwayTeamCorners"] = away_team_corners
    input_data["HomeTeamYellowCards"] = home_team_yellow_cards
    input_data["AwayTeamYellowCards"] = away_team_yellow_cards
    input_data["HomeTeamRedCards"] = home_team_red_cards
    input_data["AwayTeamRedCards"] = away_team_red_cards
    
    # Convert to a DataFrame
    input_vector = pd.DataFrame([input_data], columns=features)
    return input_vector



class MatchPredictorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Football Match Predictor")
        self.setGeometry(100, 100, 400, 600)
        self.init_ui()

    def init_ui(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        # Input fields
        self.referee_label = QLabel("Referee:")
        self.referee_input = QLineEdit()
        layout.addWidget(self.referee_label)
        layout.addWidget(self.referee_input)

        self.home_team_label = QLabel("Home Team:")
        self.home_team_input = QLineEdit()
        layout.addWidget(self.home_team_label)
        layout.addWidget(self.home_team_input)

        self.away_team_label = QLabel("Away Team:")
        self.away_team_input = QLineEdit()
        layout.addWidget(self.away_team_label)
        layout.addWidget(self.away_team_input)

        self.home_team_shots_label = QLabel("Home Team Shots:")
        self.home_team_shots_input = QLineEdit()
        layout.addWidget(self.home_team_shots_label)
        layout.addWidget(self.home_team_shots_input)
        
        self.away_team_shots_label = QLabel("Away Team Shots: ")
        self.away_team_shots_input = QLineEdit()
        layout.addWidget(self.away_team_shots_label)
        layout.addWidget(self.away_team_shots_input)
        
        self.home_team_shots_on_target_label = QLabel("Home Team Shots on Target:")
        self.home_team_shots_on_target_input = QLineEdit()
        layout.addWidget(self.home_team_shots_on_target_label)
        layout.addWidget(self.home_team_shots_on_target_input)
        
        self.away_team_shots_on_target_label = QLabel("Away Team Shots on Target:")
        self.away_team_shots_on_target_input = QLineEdit()
        layout.addWidget(self.away_team_shots_on_target_label)
        layout.addWidget(self.away_team_shots_on_target_input)
        
        self.home_team_fouls_committed_label = QLabel("Home Team Fouls Commmitted:")
        self.home_team_fouls_committed_input = QLineEdit()
        layout.addWidget(self.home_team_fouls_committed_label)
        layout.addWidget(self.home_team_fouls_committed_input)
        
        self.away_team_fouls_committed_label = QLabel("Away Team Fouls Commmitted:")
        self.away_team_fouls_committed_input = QLineEdit()
        layout.addWidget(self.away_team_fouls_committed_label)
        layout.addWidget(self.away_team_fouls_committed_input)
        
        self.home_team_corners_label = QLabel("Home Team Corners:")
        self.home_team_corners_input = QLineEdit()
        layout.addWidget(self.home_team_corners_label)
        layout.addWidget(self.home_team_corners_input)
        
        self.away_team_corners_label = QLabel("Away Team Corners:")
        self.away_team_corners_input = QLineEdit()
        layout.addWidget(self.away_team_corners_label)
        layout.addWidget(self.away_team_corners_input)
        
        self.home_team_yellow_cards_label = QLabel("Home Team Yellow Cards:")
        self.home_team_yellow_cards_input = QLineEdit()
        layout.addWidget(self.home_team_yellow_cards_label)
        layout.addWidget(self.home_team_yellow_cards_input)
        
        self.away_team_yellow_cards_label = QLabel("Away Team Yellow Cards:")
        self.away_team_yellow_cards_input = QLineEdit()
        layout.addWidget(self.away_team_yellow_cards_label)
        layout.addWidget(self.away_team_yellow_cards_input)
        
        self.home_team_red_cards_label = QLabel("Home Team Red Cards:")
        self.home_team_red_cards_input = QLineEdit()
        layout.addWidget(self.home_team_red_cards_label)
        layout.addWidget(self.home_team_red_cards_input)
        
        self.away_team_red_cards_label = QLabel("Away Team Red Cards:")
        self.away_team_red_cards_input = QLineEdit()
        layout.addWidget(self.away_team_red_cards_label)
        layout.addWidget(self.away_team_red_cards_input)
        
        # Predict button
        self.predict_button = QPushButton("Predict Match Result")
        self.predict_button.clicked.connect(self.predict_result)
        layout.addWidget(self.predict_button)

        # Prediction result labels
        self.result_1_5u_label = QLabel("1.5U Prediction: ")
        layout.addWidget(self.result_1_5u_label)

        self.result_2_5u_label = QLabel("2.5U Prediction: ")
        layout.addWidget(self.result_2_5u_label)

        self.result_home_win_label = QLabel("Home Team Win Prediction: ")
        layout.addWidget(self.result_home_win_label)

        self.result_away_win_label = QLabel("Away Team Win Prediction: ")
        layout.addWidget(self.result_away_win_label)

        self.result_draw_label = QLabel("Draw Prediction: ")
        layout.addWidget(self.result_draw_label)

        self.central_widget.setLayout(layout)

    def predict_result(self):
        try:
            # GET USER INPUTS
            # Text inputs
            referee   = self.referee_input.text()
            home_team = self.home_team_input.text()
            away_team = self.away_team_input.text()
            # Numerical inputs, convert to int
            home_team_shots = int(self.home_team_shots_input.text() or 0)
            away_team_shots = int(self.away_team_shots_input.text() or 0)
            home_team_shots_on_target = int(self.home_team_shots_on_target_input.text() or 0)
            away_team_shots_on_target = int(self.away_team_shots_on_target_input.text() or 0)
            home_team_fouls_committed = int(self.home_team_fouls_committed_input.text() or 0)
            away_team_fouls_committed = int(self.away_team_fouls_committed_input.text() or 0)
            home_team_corners = int(self.home_team_corners_input.text() or 0)
            away_team_corners = int(self.away_team_corners_input.text() or 0)
            home_team_yellow_cards = int(self.home_team_yellow_cards_input.text() or 0)
            away_team_yellow_cards = int(self.away_team_yellow_cards_input.text() or 0)
            home_team_red_cards = int(self.home_team_red_cards_input.text() or 0)
            away_team_red_cards = int(self.away_team_red_cards_input.text() or 0)
    
            # Format the input for prediction
            input_vector = format_input(referee, 
                                        home_team, 
                                        away_team, 
                                        home_team_shots,
                                        away_team_shots,
                                        home_team_shots_on_target,
                                        away_team_shots_on_target,
                                        home_team_fouls_committed,
                                        away_team_fouls_committed,
                                        home_team_corners,
                                        away_team_corners,
                                        home_team_yellow_cards,
                                        away_team_yellow_cards,
                                        home_team_red_cards,
                                        away_team_red_cards)
            print(f"Input vector for prediction:\n{input_vector}")
    
            # Predict the result for each model
            result_1_5u = models["1.5U_model"].predict(input_vector)[0]
            result_2_5u = models["2.5U_model"].predict(input_vector)[0]
            result_home_win = models["HomeTeamWin_model"].predict(input_vector)[0]
            result_away_win = models["AwayTeamWin_model"].predict(input_vector)[0]
            result_draw = models["Draw_model"].predict(input_vector)[0]

            # Update the labels with predictions
            self.result_1_5u_label.setText(f"1.5U Prediction: {result_1_5u}")
            self.result_2_5u_label.setText(f"2.5U Prediction: {result_2_5u}")
            self.result_home_win_label.setText(f"Home Team Win Prediction: {result_home_win}")
            self.result_away_win_label.setText(f"Away Team Win Prediction: {result_away_win}")
            self.result_draw_label.setText(f"Draw Prediction: {result_draw}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")


# Main application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MatchPredictorApp()
    main_window.show()
    sys.exit(app.exec_())
