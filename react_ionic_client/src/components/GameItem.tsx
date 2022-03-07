import {IonItem, IonLabel} from "@ionic/react";

type Props = {
    name: string
}

const GameItem: React.FC<Props> = (props) => {
    return (
        <IonItem routerLink={`/game/${props.name}`}>
            <IonLabel><h1>{props.name}</h1></IonLabel>
        </IonItem>    );
};

export default GameItem;
