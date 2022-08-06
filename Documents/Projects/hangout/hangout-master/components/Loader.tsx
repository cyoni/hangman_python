import React from 'react'
import Spinner from './Spinner'

function Loader() {
    return (
        <div className="absolute top-0 left-0 h-full w-full bg-gray-50 opacity-80">
          <Spinner className="absolute top-0 left-0 bottom-0 right-0 m-auto h-fit w-fit" />
        </div>
    )
}

export default Loader
