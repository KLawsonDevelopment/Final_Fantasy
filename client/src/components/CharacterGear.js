import React, { Component } from 'react';
import Axios from 'axios';

class CharacterGear extends Component {
    state = {
        character:{},
        gear:{}
    }

    componentDidMount(){
        const characterId = this.props.match.params.id
        this.getCharacter(characterId)
    }

    getCharacter = async (characterId) =>{
        try {
            const res = await Axios.get(`/api/v1/characters/${characterId}`)
            this.setState({
                character : res.data,
                gear: res.data.gear_details
            })}
        catch (err) {
            console.log(err)
        }
    }
    render() {
        return (
            <div>
                <h1>Hello World</h1>
                {this.state.character.Name}
                <img src={this.state.character.Avatar} alt={this.state.character.Name}/>
                {/* {this.state.gear.map(gear =>(
                    <div key={gear.id}>
                        <img src={gear.icon} alt="None"/>
                    </div>
                ))} */}
            </div>
        );
    }
}

export default CharacterGear;