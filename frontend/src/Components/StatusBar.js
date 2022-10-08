import React from 'react';
import './StatusBar.css';
import { MdOutlineWifi, MdNetworkCell, MdBattery20 } from 'react-icons/md';
const StatusBar = () => {
    const hour = new Date().getHours();
    const minutes = new Date().getMinutes();
    return (
        <div className="statusBar">
            <div className="statusBar__time">{hour} : {minutes > 9 ? minutes : `0${minutes}`}</div>
            <div className="statusBar__newtwork">
                <MdOutlineWifi />
                <MdNetworkCell />
                <MdBattery20 />
            </div>
        </div>
    );
}

export default StatusBar;
