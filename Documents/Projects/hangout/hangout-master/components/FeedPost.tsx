import { EmojiHappyIcon, PlusIcon, ThumbUpIcon } from "@heroicons/react/outline"
import React from "react"
import Avatar from "./Avatar"

function FeedPost() {
  return (
    <div className="mt-4 rounded-md bg-white p-2 shadow-sm">
      <div className="flex justify-between">
        <div className="flex space-x-2">
          <Avatar className="h-11 w-11" />
          <div className="flex flex-col">
            <div className="font-bold">Yoni</div>
            <div className="text-sm leading-3 ">Tel Aviv, Israel</div>
            <div className="text-xs">5m</div>
          </div>
        </div>

        <div className="flex space-x-2 justify-self-center">
          <button
            className="btn-outline  "
          >
            <div className="flex items-center space-x-2">
              <PlusIcon className="h-5" /> <span>Follow</span>
            </div>
          </button>
        </div>
      </div>
      <div className="my-2 max-h-[700px] min-h-[100px] pl-2">
        this is the post
      </div>
      <button
          className="btn-outline  "
        >
          <div className="flex h-9 px-2 items-center space-x-2">
            <ThumbUpIcon className="h-5" /> <span>Like</span>
          </div>
        </button>
    </div>
  )
}

export default FeedPost
