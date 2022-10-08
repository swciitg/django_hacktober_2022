import React from 'react'
import Row from './Row'

function CollectionRow({ heading, rowData }) {
    return (
        <div className="collection__row">
            <h2>{heading}</h2>
            {
                rowData.map((item) => (
                    <Row key={item.id} title={item.text} />
                ))
            }
        </div>
    )
}

export default CollectionRow