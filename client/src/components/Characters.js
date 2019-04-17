import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

class Characters extends Component {
    state = {
        characters: [],
        portraitDisplayed: false
    }

    componentDidMount() {
        this.getCharacters()
    }

    getCharacters = async () => {
        try {
            const res = await axios.get('/api/v1/characters');
            this.setState({ characters: res.data })
        }
        catch (err) {
            console.log(err)
        }
    }

    showPortrait = () => {
        this.setState({ portraitDisplayed: !this.state.portraitDisplayed })
    }
    render() {
        return (
            <div>
                {
                    this.state.portraitDisplayed
                        ? <div>
                            <button onClick={this.showPortrait}>Shrink</button>
                            {this.state.characters.map(character => (
                                <div key={character.id}>
                                    <Link to={`character/${character.id}`}>{character.Name}
                                    <img src={character.Portrait} alt={character.Name}/></Link>
                                </div>
                            ))}
                        </div>
                        : <div>
                            <button onClick={this.showPortrait}>Expand</button>
                            {this.state.characters.map(character => (
                                <div key={character.id}>
                                    <Link to={`character/${character.id}`}>{character.Name}</Link>
                                </div>
                            ))}
                        </div>}

            </div>
        );
    }
}

export default Characters;