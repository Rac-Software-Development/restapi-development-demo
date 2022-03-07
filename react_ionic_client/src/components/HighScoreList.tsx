import {
    IonContent,
    IonHeader,
    IonItem,
    IonLabel,
    IonList,
    IonPage,
    IonTitle,
    IonToolbar
} from "@ionic/react";
import HighScoreItem from "./HighScoreItem";
import {RouteComponentProps, useParams} from "react-router";
import {useEffect, useState} from "react";

interface HighScoreList
    extends RouteComponentProps<{
        gamename: string;
    }> {}

interface HighScores {
    name: string,
    score: number

}

const HighScoreList: React.FC<HighScoreList> = ({ match }) => {
    const [ scores, setHighScores ] = useState<HighScores[]>([]);

    const getHighScores = async () => {
        const response = await fetch("http://127.0.0.1:8080/highscores/" + match.params.gamename)
        const json = await response.json()
        setHighScores(json.scores)
    }

    useEffect(() => {
        if(scores.length == 0) {
            getHighScores()
        }
    })

    return (
        <IonPage>
            <IonHeader>
                <IonToolbar>
                    <IonTitle>{match.params.gamename}</IonTitle>
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
                        { scores.map((score, index)=> (
                            <HighScoreItem key={index} name={score.name} score={score.score} />
                        ))}
                    </IonList>
                </IonContent>
            </IonContent>
        </IonPage>
    );
};

export default HighScoreList;
