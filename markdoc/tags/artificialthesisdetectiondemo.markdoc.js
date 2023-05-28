import { ArtificialThesisDetectionGit } from '../../components/ArtificialThesisDetectionGit.js';

export default {
  render: ArtificialThesisDetectionGit,
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