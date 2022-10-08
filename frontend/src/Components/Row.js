import React from 'react'
import './Row.css'

function Row({ title }) {
    return (
        <div className="row">
            <p>{title}</p>
        </div>
    )
}

export default Row