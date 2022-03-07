import {IonItem, IonLabel} from "@ionic/react";

type Props = {
    name: string,
    score: number
}

const HighScoreItem: React.FC<Props> = (props) => {
    return (
        <IonItem>
            <IonLabel>
                <h2>{props.name}</h2>
                <h2>{props.score}</h2>
            </IonLabel>
        </IonItem>
    );
};

export default HighScoreItem;
