import React from 'react'
import './Header.css'
import { AiOutlineInfoCircle } from 'react-icons/ai'
import { BiHistory } from 'react-icons/bi'
function Header() {
    return (
        <div className='header'>
            <div className="header__logo">
                <h2>Sac Room Booking</h2>
            </div>
            <div className="header__iconContainer">
                <BiHistory className='header__icons' />
                <AiOutlineInfoCircle className='header__icons' />
            </div>
        </div>
    )
}

export default Header