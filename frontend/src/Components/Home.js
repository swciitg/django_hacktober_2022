import React from 'react'
import './Home.css'
import StatusBar from './StatusBar'
import Header from './Header'
import CollectionRow from './CollectionRow'

const ClubData = [
    {
        id: 1,
        text: 'Anchorenza and RadioG'
    },
    {
        id: 2,
        text: 'Finesse'
    },
    {
        id: 3,
        text: 'Lumeire'
    },
    {
        id: 4,
        text: 'Montage'
    },
    {
        id: 5,
        text: 'Octaves'
    },
    {
        id: 6,
        text: 'Expressions'
    },
];
const RoomData = [
    {
        id: 1,
        text: "Yoga Room"
    },
    {
        id: 2,
        text: "Sail"
    },
    {
        id: 3,
        text: "SWC"
    }
];
function Home() {
    return (
        <div className='home'>
            <StatusBar />
            <Header />
            <CollectionRow heading={"Clubs"} rowData={ClubData} />
            <CollectionRow heading={"Rooms"} rowData={RoomData} />
        </div>
    )
}

export default Home