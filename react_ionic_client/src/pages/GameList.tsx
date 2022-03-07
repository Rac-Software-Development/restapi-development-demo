import {
    IonContent,
    IonHeader,
    IonList,
    IonPage,
    IonTitle,
    IonToolbar
} from '@ionic/react';
import GameItem from "../components/GameItem";
import {useEffect, useState} from "react";


const GameList: React.FC = () => {
    const [ games, setGames ] = useState<string[]>([]);

    const getGames = async () => {
        const response = await fetch("http://127.0.0.1:8080/highscores")
        const json = await response.json()
        setGames(json)
    }

    useEffect(() => {
        if(games.length == 0) {
            getGames()
        }
    })

    return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Darts</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Blank</IonTitle>
          </IonToolbar>
        </IonHeader>
          <IonContent>
              <IonList>
                  { games.map((game, index)=> (
                      <GameItem key={index} name={game}/>
                  ))}
              </IonList>
          </IonContent>
      </IonContent>
    </IonPage>
  );
};

export default GameList;
