import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import Axios from 'axios';

class CharacterGear extends Component {
    state = {
        character: {
            Name: '',
            Portrait: '',
            Avatar: '',
            characterId: '',
        },
        gear: [],
        wantedGear: [],
        displayEditForm: false,
        redirectToHome: false,
        newGear: {
            Creator: '',
            Icon: '',
            Dye: '',
            ID: '',
            Mirage: '',
            Character: ``
        },
        newGearForm: false
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

    handleChangeCharacter = (event) => {
        const editCharacter = { ...this.state.character }
        editCharacter[event.target.name] = event.target.value

        this.setState({ character: editCharacter })
    }

    handleChangeWanted = (event) => {
        const newWanted = { ...this.state.newGear }
        newWanted[event.target.name] = event.target.value
        this.setState({ newGear: newWanted })
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
            this.setState({ redirectToHome: true })

        }
        catch (err) {
            console.log(err)
        }
    }

    newGearForm = () => {
        this.setState({
            newGearForm: !this.state.newGearForm,
            newGear: {
                Character: this.state.character.id,
                gearType: 'Body',
                Mirage: 'none',
            }
        })
    }

    newGear = async (event) => {
        event.preventDefault();
        try {
            const res = await Axios.post('/api/v1/wanted/', this.state.newGear)
            const allWanted = [...this.state.wantedGear]
            allWanted.push(res.data)
            this.setState({
                wantedGear: allWanted,
                newGear: {
                    Creator: '',
                    Icon: '',
                    Dye: '',
                    ID: '',
                    Mirage: '',
                    Character: ''
                },
                newGearForm: false
            },
            )
        }
        catch (err) {
            console.log(err)
        }
    }

    importGear = async () => {
        try {
            let res = await Axios.get(`https://xivapi.com/character/${this.state.character.characterId}`)

            let GearSet = res.data.Character.GearSet.Gear
            for (const key in GearSet) {
                if (GearSet.hasOwnProperty(key)) {
                    let GearSetIconData = await Axios.get(`https://xivapi.com/item/${GearSet[key].ID}`)
                    let GearSetIcon = GearSetIconData.data.Icon
                    const Gear = [...this.state.gear]
                    this.setState({
                        newGear: {
                            Creator: GearSet[key].Creator,
                            Icon: `https://xivapi.com/${GearSetIcon}`,
                            Dye: GearSet[key].Dye,
                            ID: GearSet[key].ID,
                            Mirage: GearSet[key].Mirage,
                            Character: this.state.character.id,
                            gearType: key
                        },
                    })
                    Gear.push(this.state.newGear)
                    this.setState({
                        gear: Gear
                    })
                    let res2 = await Axios.post('/api/v1/pieces/', this.state.newGear)
                }
            }

        }
        catch (err) {
            console.log(err)
        }
    }

    deleteGear = async () => {
        try {
            let arr1 = this.state.gear
            for (let i=0; i<arr1.length; i++) {
                Axios.delete(`/api/v1/pieces/${arr1[i].ID}`)
            }
            this.setState({ gear: [] })
        }
        catch (err) {
            console.log(err)
        }
    }


    render() {
        if (this.state.redirectToHome === true) {
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
                                onChange={this.handleChangeCharacter} />
                            <button>Submit</button>
                        </form>
                        : <div>
                            <h1>Current Gear</h1>
                            {this.state.character.Name}
                            <img src={this.state.character.Avatar} alt={this.state.character.Name} />
                            <button onClick={this.importGear}>Import</button>
                            <button onClick={this.deleteGear}>Delete Current Gear</button>
                            {this.state.gear.map(gear => (
                                <div key={gear.ID}>
                                    <img src={gear.Icon} alt={gear.ID} />
                                </div>
                            ))}
                            <h2>Wanted Gear</h2>
                            <button onClick={this.newGearForm}>New</button>
                            {
                                this.state.newGearForm
                                    ? <form onSubmit={this.newGear}>
                                        <label htmlFor="Creator">Creator:</label>
                                        <input type="text"
                                            id="Creator"
                                            name="Creator"
                                            value={this.state.newGear.Creator}
                                            onChange={this.handleChangeWanted} />

                                        <label htmlFor="Icon">Icon:</label>
                                        <input type="text"
                                            id="Icon"
                                            name="Icon"
                                            value={this.state.newGear.Icon}
                                            onChange={this.handleChangeWanted} />
                                        <label htmlFor="Dye">Dye:</label>
                                        <input type="text"
                                            id="Dye"
                                            name="Dye"
                                            value={this.state.newGear.Dye}
                                            onChange={this.handleChangeWanted} />
                                        <button>Submit</button>
                                    </form>
                                    :
                                    <div>
                                        {this.state.wantedGear.map(wanted => (
                                            <div key={wanted.ID}>
                                                <img src={wanted.Icon} alt={wanted.Id} />
                                            </div>
                                        ))}
                                    </div>
                            }
                        </div>
                }
            </div>
        );
    }
}

export default CharacterGear;