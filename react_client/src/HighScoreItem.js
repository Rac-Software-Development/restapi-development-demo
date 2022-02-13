import './HighScore.css';
import React from 'react';

class HighScoreItem extends React.Component {
    render() {
        return (
            <>  {/* A "React fragment", see https://stackoverflow.com/questions/31284169/parse-error-adjacent-jsx-elements-must-be-wrapped-in-an-enclosing-tag  */}
                <dt>{this.props.name}</dt>
                <dd>{this.props.value}</dd>
            </>
        )
    }
}

export default HighScoreItem;
