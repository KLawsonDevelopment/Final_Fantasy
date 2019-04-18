import React, { Component } from 'react';
import {Redirect} from 'react-router-dom';
import Axios from 'axios';

class CharacterGear extends Component {
    state = {
        character: {},
        gear: [],
        wantedGear: [],
        displayEditForm: false,
        redirectToHome: false
    }

    componentDidMount() {
        const characterId = this.props.match.params.id
        this.getCharacter(characterId)
    }

    getCharacter = async (characterId) => {
        try {
            const res = await Axios.get(`/api/v1/characters/${characterId}`)
            this.setState({
                character: res.data,
                gear: res.data.GearPieces,
                wantedGear: res.data.wantedgear
            })
        }
        catch (err) {
            console.log(err)
        }
    }

    handleChange = (event) => {
        const editCharacter = { ...this.state.character }
        editCharacter[event.target.name] = event.target.value

        this.setState({ character: editCharacter })
    }

    showEdit = () => {
        this.setState({ displayEditForm: !this.state.displayEditForm })
    }

    updateCharacter = async (event) => {
        event.preventDefault();
        try {
            const res = await Axios.put(`/api/v1/characters/${this.props.match.params.id}/`, this.state.character)
            this.setState({
                character: res.data,
                displayEditForm: false
            })
        }
        catch (err) {
            console.log(err)
        }
    }

    deleteCharacter = async () => {
        try {
            await Axios.delete(`/api/v1/characters/${this.props.match.params.id}`)
            this.setState({redirectToHome: true})
            
        }
        catch (err) {
            console.log(err)
        }
    }


    render() {
        if (this.state.redirectToHome===true) {
            return <Redirect to='/'></Redirect>
        }
        return (
            <div>
                <button onClick={this.showEdit}>Edit</button>
                <button onClick={this.deleteCharacter}>Delete</button>
                {
                    this.state.displayEditForm
                        ? <form onSubmit={this.updateCharacter}><label htmlFor="Name">Name:</label>
                            <input type='text'
                                id='Name'
                                name='Name'
                                value={this.state.character.Name}
                                onChange={this.handleChange} />
                            <button>Submit</button>
                        </form>
                        : <div>
                            <h1>Current Gear</h1>
                            {this.state.character.Name}
                            <img src={this.state.character.Avatar} alt={this.state.character.Name} />
                            {this.state.gear.map(gear => (
                                <div key={gear.ID}>
                                    <img src={gear.Icon} alt={gear.ID} />{gear.Name}
                                </div>
                            ))}
                            <h2>Wanted Gear</h2>
                            {this.state.wantedGear.map(wanted => (
                                <div key={wanted.ID}>
                                    <img src={wanted.Icon} alt={wanted.Id} />
                                </div>
                            ))}
                        </div>
                }
            </div>
        );
    }
}

export default CharacterGear;