import './HighScore.css';
import React from 'react';
import HighScoreItem from "./HighScoreItem";

class HighScoreList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            lastScores: []
        };
    }

    componentDidMount() {
        let gettingScores = setInterval(() => {
            this.getHighScores()
        }, 2000);
        this.setState({gettingScores: gettingScores} )
    }

    getHighScores() {
        fetch('http://127.0.0.1:5001/highscores/lunarlander')
            .then(response => response.json())
            .then(data => this.setState({ lastScores: data.scores }))
            .catch(error => {console.error('Error:', error);
        });
    }

    render() {
        return (
            <div className="App">
                HIGHSCORES:
                <dl id="scorelist">
                    {this.state.lastScores.map((score, index) =>
                    <HighScoreItem key={index} name={score.name} value={score.score}/>
                    )}
                </dl>
            </div>
        )
    }
}

export default HighScoreList;
