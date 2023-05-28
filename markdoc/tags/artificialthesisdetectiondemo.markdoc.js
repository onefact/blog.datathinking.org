import { ArtificialThesisDetectionDemo } from '../../components/ArtificialThesisDetectionDemo.js';

export default {
  render: ArtificialThesisDetectionDemo,
  attributes: {
    src: {
      type: String,
      required: true
    },
    title: {
      type: String,
      required: true
    },
    width: {
      type: String,
      default: '50%'
    }
  }
};