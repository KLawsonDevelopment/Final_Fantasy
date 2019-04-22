import React, { Component } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';

class Characters extends Component {
    state = {
        characters: [],
        newCharacter: {
            Name: '',
            Portrait: '',
            Avatar: '',
            characterId: ''
        },
        portraitDisplayed: false,
        newCharacterForm: false,
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

    newCharacterForm = () => {
        this.setState({ newCharacterForm: !this.state.newCharacterForm })
    }

    handleChange = (event) => {
        const newCharacter = { ...this.state.newCharacter }
        newCharacter[event.target.name] = event.target.value
        this.setState({ newCharacter: newCharacter })
    }

    newCharacter = async (event) => {
        event.preventDefault();
        try {
            const res = await axios.post('/api/v1/characters/', this.state.newCharacter)
            const allCharacters = [...this.state.characters]
            allCharacters.push(res.data)
            this.setState({
                characters: allCharacters,
                newCharacter: {
                    Name: '',
                    Portrait: '',
                    Avatar: '',
                },
                newCharacterForm: false
            })
        }
        catch (err) {
            console.log(err)
        }
    }

    importCharacter = async () =>{
        try{
            let importedValue = document.getElementById("import").value
            let res = await axios.get(`https://xivapi.com/character/search?name=${importedValue}&server=Malboro`)
            let importedCharacter = await axios.get(`https://xivapi.com/character/${res.data.Results[0].ID}`)
            this.setState({
                newCharacter: {
                    Name: importedCharacter.data.Character.Name,
                    Portrait: importedCharacter.data.Character.Portrait,
                    Avatar: importedCharacter.data.Character.Avatar,
                    characterId: importedCharacter.data.Character.ID
                }
            })
            res = await axios.post('/api/v1/characters/', this.state.newCharacter)
            const allCharacters = [...this.state.characters]
            allCharacters.push(res.data)
            this.setState({
                characters: allCharacters,
                newCharacter: {
                    newCharacter: '',
                    Portrait: '',
                    Avatar: '',
                }
            })
        }
        catch (err) {
            console.log(err)
        }
    }


    render() {
        return (
            <div>
                
                {
                    this.state.newCharacterForm
                        ? <div>
                            <button onClick={this.newCharacterForm}>Reverse</button>
                            <form onSubmit={this.newCharacter}>
                                <div>
                                    <label htmlFor="Name">Name:</label>
                                    <input type='text'
                                        id='Name'
                                        name='Name'
                                        onChange={this.handleChange} />
                                </div>
                                <div>
                                    <label htmlFor="Portrait">Portrait:</label>
                                    <input type='text'
                                        id='Portrait'
                                        name='Portrait'
                                        onChange={this.handleChange} />
                                </div>
                                <div>
                                    <label htmlFor="Avatar">Avatar:</label>
                                    <input type='text'
                                        id='Avatar'
                                        name='Avatar'
                                        onChange={this.handleChange} />
                                </div>
                                <button>Submit</button>
                            </form>
                        </div>

                        : <div>{
                            this.state.portraitDisplayed
                                ? <div>
                                    <button onClick={this.newCharacterForm}>New Character</button>
                                    <button onClick={this.showPortrait}>Shrink</button>
                                    {this.state.characters.map(character => (
                                        <div key={character.id}>
                                            <Link to={`character/${character.id}`}>{character.Name}
                                                <img src={character.Portrait} alt={character.Name} /></Link>
                                        </div>
                                    ))}
                                </div>
                                : <div>
                                    <button onClick={this.newCharacterForm}>New Character</button>
                                    <button onClick={this.showPortrait}>Expand</button>
                                    {this.state.characters.map(character => (
                                        <div key={character.id}>
                                            <Link to={`character/${character.id}`}>{character.Name}</Link>
                                        </div>
                                    ))}
                                    <button onClick={this.importCharacter}>Import</button>
                                    <input type="text" id="import"/>
                                </div>
                        }</div>
                }

            </div>
        );
    }
}

export default Characters;